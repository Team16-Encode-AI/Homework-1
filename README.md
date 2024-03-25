# Homework-1
The project contains homework assigned for week 1 of encode AI bootcamp.

There are two main parts of this exercise. Firstly, there are three functionalities that the chatbot needs to provide, and secondly, we want to test how the output is affected by different descriptions of the chef personality/characteristic.

## Functionalities:

1. Provide a recipe given a name for a dish.
2. Provide a recipe given an ingredient.
3. Critique provided recipe.

We have looked at two ways of introducing these functionalities to prompts:
- ask the user to explicitly choose a functionality and then tailor a prompt for that functionality
- include description of these 3 functionalities in a prompt, which means that when the chatbot predicts the answer, there is an implicit step of recognising the task from the user input.

On the small set of examples, we found that it is not necessary to have the user explicitly declare the functionality they seek.


## Chef's description

There are various ways how we can describe the chef, for example:

- **Experience** 
- **Humor / rudeness** 
- **Poetic Expression**
- **Conciseness** 


It is interesting to notice the interactions between different elements of the prompt setting. For example if in the description of task we write “If you recognise the name of a dish, you must answer directly with a detailed recipe for it” will it mean that the output will always be detailed regardless of how we describe the chef? It turns out that:
- if the description includes “You usually are annoyed, don't like helping others and often believe that you know better what other needs.” – the result is clear and detailed
- if the description also adds “You know a lot about different cuisines and cooking techniques, but don't like to share the knowledge and don't mind if the recipes are correct.” - the recipes are still very clear,
- adding information that the could prefer to spew profanities than help “You can also provide tips and tricks for cooking and food preparation, but prefer to spew profanities instead.” - changes the wording of the output only slightly
- however the explicit mentioning of not listening to instructions “ You usually are annoyed, don't like helping others and don't listen to instructions. “ - this is what eventually overrides the description from the task, and changes detailed output into short and often too generic.


Other observations:
- changing wording of “experienced” to “inexperienced” doesn’t have noticeable effect 
- changing wording of “experienced” to “newbie” did have much more pronounced effect.


## Improvements if we had more time

Note into the report we have not made a verification system to check if api_key entered by user is valid. We have asked for the user to provide the key rather than look for environmental variable or read from a file - as this was easier to ensure the script works with various settings and systems.

     
  
