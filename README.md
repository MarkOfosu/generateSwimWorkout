# `Swim Workout Generator`

This project is a web application that generates swim workouts based on user input. It utilizes the LangChain framework and OpenAI's GPT-4 model to create customized swim workouts, including warm-up, main sets, and cooldowns.

### Features
- Generate customized swim workouts
- User-friendly interface using Streamlit
- Leverages GPT-4 for generating workouts with structured output

## 🛠 Technologies Used
- **Python**
- **Streamlit**: For building the web interface
- **LangChain**: For managing and interacting with the GPT-4 model
- **Pydantic**: For data validation and settings management
- **OpenAI API**: For generating the swim workouts

## 🚀 Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- An OpenAI API key (to access GPT-4)

### 1. Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/markofosu/swim-workout-generator.git
cd swim-workout-generator

2. Set Up Virtual Environment (Optional but Recommended)
It’s recommended to use a virtual environment to manage your project dependencies:

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install Dependencies
Navigate into the project directory and install the required Python packages:

pip install -r requirements.txt


4. Set Up Environment Variables
Create a .env file in the project root directory and add your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key_here


5. Run the Application
Start the Streamlit application by running:

streamlit run main.py


6. Access the Application
Open your browser and go to:

http://localhost:
Enter your workout request in the input box, and click "Generate Workout" to see your customized swim workout.

🧑‍💻 Project Structure
main.py: The main entry point for the Streamlit application.
langchain_helper.py: Contains the logic for interacting with LangChain and generating the swim workouts.
system_training_data.py: Includes the system's predefined training data for generating workouts.
📜 Example Workouts
Here are a few examples of workout prompts you can try:

- Generate a speed swim workout
- Generate a mid-distance swim workout
- Generate an anaerobic swim workout


🛠 Structured Output Parser
This project leverages LangChain's structured output parsing to ensure that the generated swim workouts are formatted consistently. The SwimWorkout Pydantic model defines the expected structure of the output, which includes fields like focus, warmup, main_set, cooldown, distance, duration, intensity, and description.

To generate structured workouts:

from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List, Optional

class SwimWorkout(BaseModel):
    focus: Optional[str] = Field(description="Focus of the workout")
    warmup: List[str] = Field(description="Warm-up set")
    preset: List[str] = Field(description="Preset set")
    main_set: List[str] = Field(description="Main set")
    cooldown: List[str] = Field(description="Cool-down set")
    distance: Optional[str] = Field(description="What is the total distance of the workout")
    duration: Optional[str] = Field(description="What is the total estimated duration of the workout")
    intensity: Optional[str] = Field(description="Intensity level of the workout")
    description: Optional[str] = Field(description="Describe the workout")
You can integrate this with the LangChain framework to parse and structure the output automatically, ensuring consistency in the generated workout plans.
