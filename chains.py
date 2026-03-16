import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()


class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("API_KEY"),
                            model_name="meta-llama/llama-4-scout-17b-16e-instruct")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
           You are Akash, currently working as an intern at Airtel with experience in AI, software development, and building automation solutions.

Your task is to write a personalized cold email to a potential client regarding the job mentioned above. In the email, explain how your technical skills, problem-solving ability, and experience working with modern technologies can help address the client's requirements.

Highlight your interest in collaborating, building scalable solutions, and delivering efficient results. Maintain a professional, concise, and persuasive tone.

Also include the most relevant portfolio links from the following list to showcase your work and projects:
{link_list}

Guidelines:
- The email should be professional and concise.
- Clearly connect the client's requirements with your skills and experience.
- Briefly introduce yourself and your background.
- Naturally include the relevant portfolio links.

Remember you are Akash, an intern at Airtel.
Do not include any preamble or explanation.
Only output the final cold email.
            ### EMAIL (NO PREAMBLE):

            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content


if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))
