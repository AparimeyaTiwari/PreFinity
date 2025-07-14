import requests
import json
from typing import List, Dict, Any
import os
from dotenv import load_dotenv

class OpenRouterQuizGenerator:
    def __init__(self, api_key: str):
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
    def generate_quiz(self, user_context: Dict = None) -> Dict[str, Any]:
        """Generate personalized quiz using LLM"""
        prompt = self._build_quiz_generation_prompt(user_context)
        payload = {
            "model": "deepseek/deepseek-chat-v3-0324:free",
            "messages": [{"role": "user", "content": prompt}]
        }
        
        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            response.raise_for_status()
            
            response_json = response.json()
            content = response_json["choices"][0]["message"]["content"]
            
            # Remove Markdown code block markers if present
            if content.startswith("```json") and content.endswith("```"):
                content = content[7:-3].strip()  # Remove ```json and ```
            
            # print("Content to parse:", repr(content))  # Add this before json.loads
            quiz_data = json.loads(content)
            return self._validate_quiz_structure(quiz_data)
        except requests.exceptions.RequestException as e:
            raise ValueError(f"API request failed: {str(e)}")
        except (json.JSONDecodeError, KeyError) as e:
            raise ValueError(f"Failed to parse LLM quiz response: {content}") from e

    def _build_quiz_generation_prompt(self, user_context: Dict) -> str:
        """Construct the prompt for quiz generation"""
        base_prompt = """Generate a 10-question quiz in RAW JSON format ONLY (no Markdown code blocks, no other text or explanation) with the following structure:
        {
            "quiz_title": "Shopping Personality Quiz",
            "questions": [
                {
                    "text": "question text",
                    "type": "likert|multiple_choice",
                    "options": ["option1", ...],
                    "trait": "personality_trait_or_lifestyle_category",
                    "weight": 0.0-1.0
                }
            ],
            "scoring_rules": {
                "trait_name": {
                    "positive_indicators": [question_indices...],
                    "negative_indicators": [question_indices...]
                }
            }
        }
        The quiz should help recommend Walmart products by identifying personality traits and lifestyle preferences.
        The quiz should use these specific traits in scoring_rules: price_sensitive, health_conscious, brand_loyal, adventurous_shopper.
        All questions must use one of these traits.
        """
        
        if user_context:
            return f"{base_prompt}\n\nUser context: {json.dumps(user_context)}"
        return base_prompt

    def _validate_quiz_structure(self, quiz_data: Dict) -> Dict:
        """Ensure the generated quiz meets requirements"""
        required_fields = ["quiz_title", "questions", "scoring_rules"]
        if not all(field in quiz_data for field in required_fields):
            raise ValueError("Invalid quiz structure from LLM")
        
        for question in quiz_data["questions"]:
            if "text" not in question or "trait" not in question:
                raise ValueError("Invalid question format")
        
        return quiz_data
    
class QuizEvaluator:
    def __init__(self, generator: OpenRouterQuizGenerator):
        self.generator = generator
        self.current_quiz = None
        
    def generate_new_quiz(self, user_context: Dict = None) -> Dict:
        """Generate and store a new quiz"""
        self.current_quiz = self.generator.generate_quiz(user_context)
        return {
            "title": self.current_quiz["quiz_title"],
            "questions": [
                {k: v for k, v in q.items() if k != "weight"} 
                for q in self.current_quiz["questions"]
            ]
        }
    
    def evaluate_responses(self, user_answers: Dict[int, Any]) -> Dict[str, float]:
        """Calculate personality/lifestyle scores from answers"""
        if not self.current_quiz:
            raise ValueError("No active quiz to evaluate")
            
        # Initialize with all traits found in questions
        traits = set(q["trait"] for q in self.current_quiz["questions"])
        trait_scores = {trait: 0.0 for trait in traits}
        
        for q_idx, answer in user_answers.items():
            try:
                if q_idx >= len(self.current_quiz["questions"]):
                    continue
                    
                question = self.current_quiz["questions"][q_idx]
                trait = question["trait"]
                weight = question.get("weight", 0.5)
                
                if question["type"] == "likert":
                    trait_scores[trait] += (answer - 3) * weight
                elif question["type"] == "multiple_choice":
                    if answer in question["options"]:
                        trait_scores[trait] += weight
            except KeyError:
                continue
        
        # Normalize scores
        max_score = max(trait_scores.values()) if trait_scores else 1
        return {t: (s/max_score) for t, s in trait_scores.items()}
    
def main():
    # Load environment variables
    load_dotenv()
    API_KEY = os.getenv("QUIZ_API")
    
    # Initialize components
    generator = OpenRouterQuizGenerator(api_key=API_KEY)
    evaluator = QuizEvaluator(generator)
    
    # Step 1: Generate quiz (could use any known user data for personalization)
    quiz = evaluator.generate_new_quiz()
    # print(f"Generated Quiz: {quiz['title']}")
    # print(quiz["questions"])

if __name__ == "__main__":
    main()