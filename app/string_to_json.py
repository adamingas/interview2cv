from typing import Dict, Any
import anthropic
import json
from typing import Optional
import os

key = ""

# Get the directory path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the JSON file in the same directory
json_file_path = os.path.join(current_dir, "template.json")
print(f"Looking for JSON file at: {json_file_path}")

    
# Load the JSON data
try:
    with open(json_file_path, 'r') as file:
        CV_TEMPLATE = json.load(file)
    
    print(f"Successfully loaded CV template for {CV_TEMPLATE.get('personalInformation', {}).get('name', 'No name provided')}")
except Exception as e:
    print(f"Unexpected error: {e}")
    CV_TEMPLATE = {
    "personalInformation": {
        "name": "",
        "title": "",
        "email": "",
        "location": {
        "city": "",
        "country": "",
        },
        "profileSummary": ""
    },
    "education": [
        {
        "degree": "",
        "institution": "",
        "location": "",
        "startDate": "",
        "endDate": "",
        "gpa": "",
        "relevantCourses": [],
        "thesis": {
            "title": "",
            "description": "",
        }
        }
    ],
    "workExperience": [
        {
        "position": "",
        "company": "",
        "location": "",
        "startDate": "",
        "endDate": "",
        "isCurrent": False,
        "description": "",
        "responsibilities": [],
        "technologies": []
        }
    ],
    "skills": {
        "technical": [
        {
            "name": "",
            "proficiency": ""
        }
        ],
        "languages": [
        {
            "language": "",
            "proficiency": ""
        }
        ],
        "soft": []
    },
    "interests": []
    }


def conversation_to_json(conversation: str, template: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Convert a conversation between LLM and user about CV details into a structured JSON format.
    
    Args:
        conversation (str): The conversation string containing CV information
        template (Dict[str, Any], optional): Custom JSON template. If None, uses default CV_TEMPLATE
    
    Returns:
        Dict[str, Any]: Structured CV data in JSON format
    """
    # Use default template if none provided
    
    try:
        # Initialize Anthropic client
        client = anthropic.Anthropic(api_key=key)
        
        prompt = f"""
        Given the following conversation about a person's CV/resume, extract the information and format it according to the template structure below.
        Only include information that was explicitly mentioned in the conversation.
        
        Template structure:
        {json.dumps(CV_TEMPLATE, indent=2)}
        
        Conversation:
        {conversation}
        
        Please format the extracted information as valid JSON following the template structure.
        Only include fields that have information from the conversation.
        """
        
        # Get Claude's response
        message = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            temperature=0,
            system="You are a precise JSON formatter. Extract information from conversations and format them exactly according to the provided template structure. Only include information explicitly mentioned in the conversation.",
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        # Parse the response to get JSON
        # We expect Claude to return valid JSON string
        response_content = message.content[0].text
        # Find the JSON part in Claude's response (assuming it might include other text)
        json_start = response_content.find('{')
        json_end = response_content.rfind('}') + 1
        json_str = response_content[json_start:json_end]
        
        # Parse and validate the JSON
        cv_data = json.loads(json_str)
        
        with open('cv_data.json', 'w') as file:
            json.dump(cv_data, file, indent=2)

        return cv_data
        
    except anthropic.APIError as e:
        raise Exception(f"Error calling Anthropic API: {str(e)}")
    except json.JSONDecodeError as e:
        raise Exception(f"Error parsing JSON response: {str(e)}")
    except Exception as e:
        raise Exception(f"Unexpected error: {str(e)}")

# Example usage:
if __name__ == "__main__":
    # Example conversation
    sample_conversation = '''
    LLM: What is your full name?
    User: John Doe
    LLM: What's your email address?
    User: john.doe@email.com
    LLM: Could you share your educational background?
    User: I have a Bachelor's in Computer Science from MIT, graduated in 2020
    LLM: What about your work experience?
    User: I worked at Google as a Software Engineer for 2 years, mainly developing cloud infrastructure
    LLM: What are your key skills?
    User: Python, JavaScript, Cloud Computing, and Machine Learning
    '''
    
    try:
        result = conversation_to_json(sample_conversation)
        
    except Exception as e:
        print(f"Error: {str(e)}")