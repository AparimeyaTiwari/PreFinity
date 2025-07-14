### Knowledge Graph Schema Design

(User)

  │
  ├──[:PURCHASED {date, quantity}]→ (Product)
  ├──[:VIEWED]→ (Product)
  ├──[:HAS_PERSONALITY_TRAIT]→ (Trait:Extraversion)
  ├──[:HAS_LIFESTYLE]→ (Lifestyle:OutdoorEnthusiast)
  └──[:DEMOGRAPHICS]→ (Demographics:Age_30_40)

(Product)
  ├──[:BELONGS_TO]→ (Category:Electronics)
  ├──[:HAS_ATTRIBUTE]→ (Attribute:Wireless)
  └──[:COMPLEMENTARY]→ (Product:CarryingCase)


## Assessment Design

### Personality Quiz (Based on Big Five Model)

**10-item short form with product relevance:**

1. "I enjoy trying new and unusual products"
   * Strongly disagree → [ ] Disagree → [ ] Neutral → [ ] Agree → [ ] Strongly agree
     *(Measures Openness)*
2. "I always read product reviews before purchasing"
   * Strongly disagree → [ ] Disagree → [ ] Neutral → [ ] Agree → [ ] Strongly agree
     *(Measures Conscientiousness)*
3. "I often buy products that catch my eye in the store"
   * Strongly disagree → [ ] Disagree → [ ] Neutral → [ ] Agree → [ ] Strongly agree
     *(Measures Impulsiveness/Extraversion)*

### Lifestyle Questionnaire

**7-item multi-select:**

1. Which activities describe you?
   * Outdoor sports
   * Home cooking
   * DIY projects
   * Tech gadgets
   * Fashion trends
2. How would you describe your shopping style?
   * Budget-conscious
   * Premium quality seeker
   * Eco-friendly
   * Convenience-focused
