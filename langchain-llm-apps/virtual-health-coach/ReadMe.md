<a name="readme-top"></a>


<!-- TABLE OF CONTENTS -->
## Table of Contents
  <ol>
    <li>
      <a href="#about-the-project">Project Overview:</a>
      <ul>
        <li><a href="#built-with">Technologies used:</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>  
        <li><a href="#instrumentation">Instrumentation</a></li>  
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Project Enhancements</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>

<!-- ABOUT THE PROJECT -->
## Project Overview:

**TL;DR (Brief summary):** This project showcases an AI assistant that provides plant based health advice based on a YouTube video.



**Project Inspiration:** In the United States, approximately [80% of the population](https://thedesireddesk.com/what-percentage-of-americans-work-desk-jobs/) holds sedentary jobs. This lifestyle, characterized by insufficient physical activity and often coupled with poor nutritional choices, can lead to various chronic diseases. To combat this issue, there are several strategies that workers can adopt to enhance their health. One effective approach is transitioning to a plant-based lifestyle. To facilitate this change, a user-friendly AI health app has been developed, serving as a Virtual Health Coach. This app enables users to input any health-related questions they have, providing personalized guidance and support in adopting healthier habits.


## Technologies used in this project:

#### **Hardware:** 
| **TOOL**       | **TYPE**| **Operating System**| **Version**| **Comments**
| :----------------: | :------: |  :------: | :----: |  :----: | 
| MacBook Pro         |   Hardware Device | MacOS | Ventura 13.6.1 | Used for the development of the project.

#### **Software:**
| **TOOL**       | **TYPE**| **Version**| **Comments**
| :----------------: | :------: | :----: |  :----: | 
| Visual Studio Code (VSCode)         |   Text Editor  | 1.76.2 | Used for the development of the project.
| Python         |   Programming Language   | 3.11.2 | Used to develop the project.
| FAISS       |  Vector source | 1.7.4 | The Facebook Artificial Intelligence Similarity Search was used as the vector source.
| OpenAI         |   LLM   | latest | Used as the Large Language Model (LLM). The Chat GPT-3.5 `gpt-3.5-turbo-instruct` model is being used. 
| LangChain       |  Python Framework  | latest | The framework used to facilitate the creation and development of the Virtual Health Coach app, that leverages the OpenAI LLM.
| YouTube       |  Video Sharing Platform  | latest | An American online video sharing platform.
| StreamLit       | Interactive data app creation tool | latest | This was used to build an interactive UI for users to engage with the application.









<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
- Ensure that you have access to a variation of the technologies listed in the **Technologies used in this project** section of this file.

### Installation
1. Open up the Mac Terminal.
2. Create a directory `mkdir techievibez` (to keep the project organized).
3. Navigate into that directory via `cd techievibez`.
4. Create a virtual environment `python3 -m venv aiVirtualEnv`.
5. Activate the newly created virtual environment to use, via `source aiVirtualEnv/bin/activate`. You will now enter into the virtual environment.
6. Copy the project files via `git clone https://github.com/SadeCJohnson/ai-development.git`
7. Navigate to the folder that contains the Virtual Health Coach via ` cd ai-development/langchain-llm-apps/virtual-health-coach`
8. To install all of the required tools to get this project up and running (found in the `requirements.txt` file), run `pip3 install -r requirements.txt`.
9. Launch the application via `streamlit run main.py`.
10. At this point, you might've come across this error when trying to launch the application:
![Open AI Key Required](/langchain-llm-apps/virtual-health-coach/supporting-images/OPENAI-Key-Required.png)
11. To resolve this error, head over to OpenAI's documentation to 
  * [Sign up for an OpenAI account](https://platform.openai.com/signup)
  * Visit the **API Keys** page to [Create a new secret key](https://platform.openai.com/account/api-keys). Carefully follow the instructions presented to you during this creation process.
12. Now that you have an API key, you'll need to save it as an environment variable so you can use it to access the application. To do this:
  * Run `vi ~/.zshrc` on the terminal
  * When in the **vi text editor**, select the letter `i` on the keyboard. Copy and paste this configuration `export OPENAI_API_KEY='your-api-key-here'` into the file.
  * Once you've added your OpenAI API Key to the file, press the `ESC` key, then `wq!`, and finally the `RETURN` key. This saves the OpenAI API key as an environment variable.
  * To ensure this OpenAI API key is being picked up by the application, load it via the `source ~/.zshrc` command, followed by pressing the `RETURN` key. [***Note: Executing this step will cause you to exit the virtual environment. You'll need to navigate back to the directory where the virtual environment was initially created  (see step 3 and step 5).***]
  * Verify the setup by typing in `echo $OPENAI_API_KEY` into the terminal window, followed by pressing the `RETURN` key. 
13. Navigate to the project files via `cd ai-development/langchain-llm-apps/virtual-health-coach/`.
14. Relaunch the application via `streamlit run main.py`. You should see something like the following:
![Virtual Health Coach Demo](/langchain-llm-apps/virtual-health-coach/supporting-images/VirtualHealthCoachDemo.gif)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Instrumentation
* To instrument this Python application with the New Relic platform, follow the [Python Agent Installation guide](https://newrelic.com/instant-observability/python). 
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Usage Purpose -->
## Usage
* Looking to enhance the quality of your life and align it more with the plantbased lifestyle, try using this app. If you have any feedback, please feel free to let me know or fork this repo and enhance it yourself!
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Project Enhancements -->
## Project Enhancements
 * Improve the UI / Implement a better design.
 * Add additional resources to make the chatbot more knowledgeable.
  * Right now, a single YouTube video is the sole source of information, but pdfs, ebooks, etc can be added.
 * Experiment with other LLMs to measure and compare the performance of each, to essentially select the best one. 
<p align="right">(<a href="#readme-top">back to top</a>)</p>








<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [YouTube Assistant Idea](https://github.com/rishabkumar7/youtube-assistant-langchain?tab=readme-ov-file)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template/tree/master)
* [Simon Hill PROVES The Merits of A PLANT-BASED DIET | Rich Roll Podcast](https://www.youtube.com/watch?v=a3PjNwXd09M)
<p align="right">(<a href="#readme-top">back to top</a>)</p>
