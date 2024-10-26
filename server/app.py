from llm_setup import convert_to_json, localllm, embeddings, text_splitter_semantic
from setup_RAG import query_rag
from setup_vectordb import generate_pdf, extract_data, save_to_chroma
from langchain_community.chat_models import ChatOllama
import datetime

job_desc = """
About the job
Meta is seeking AI Software Engineers to join our Research & Development teams. The ideal candidate will have industry experience working on Language related topics. The position will involve taking these skills and applying them to solve for some of the most crucial & exciting problems that exist on the web. We are hiring in multiple locations.

Software Engineer - Language (Technical Leadership) Responsibilities:

Apply relevant AI and machine learning techniques to build intelligent rich language systems that improve Meta's products and experiences
Assist in goal setting related to project impact, AI system design, and ML excellence
Develop custom/novel architectures, define use cases, and develop methodology & benchmarks to evaluate different approaches
Apply in-depth knowledge of how the machine learning system interacts with the other systems around it
Technically lead in a team environment across multiple scientific and engineering disciplines, making the architectural trade-offs required to rapidly deliver software solutions
Mentor other AI Engineers & improve the quality of AI work in the broader team
Drive the team's goals and technical direction to pursue opportunities that make your larger organization more efficient
Effectively communicate complex features and systems in detail
Write clean readable code, debug complex problems that span systems, prioritize ruthlessly and get things done with a high level of efficiency
Understand industry & company-wide trends to help assess & develop new technologies
Partner & collaborate with organization leaders to help improve the level of performance of the team & organization
Identify new opportunities for the larger organization & influence the appropriate people for staffing/prioritizing these new ideas

Minimum Qualifications:

Bachelor's degree in Computer Science, Computer Engineering, relevant technical field, or equivalent practical experience.
Specialized experience in one or more of the following machine learning/deep learning domains: Language: NLP, ASR, TTS, Conversational AI
Experience developing language algorithms or language infrastructure in C/C++ or Python

Preferred Qualifications:

Experience in deep learning and PyTorch
Experience with distributed systems or on-device algorithm development
Experience contributing to AI Publications
Proven track record of planning multi-year roadmap in which shorter-term projects ladder to the long term-vision
Experience in driving large cross-functional/industry-wide engineering efforts
Significant experience in mentoring/influencing senior engineers across organizations

About Meta:

Meta builds technologies that help people connect, find communities, and grow businesses. When Facebook launched in 2004, it changed the way people connect. Apps like Messenger, Instagram and WhatsApp further empowered billions around the world. Now, Meta is moving beyond 2D screens toward immersive experiences like augmented and virtual reality to help build the next evolution in social technology. People who choose to build their careers by building with us at Meta help shape a future that will take us beyond what digital connection makes possible today—beyond the constraints of screens, the limits of distance, and even the rules of physics.

Meta is proud to be an Equal Employment Opportunity and Affirmative Action employer. We do not discriminate based upon race, religion, color, national origin, sex (including pregnancy, childbirth, or related medical conditions), sexual orientation, gender, gender identity, gender expression, transgender status, sexual stereotypes, age, status as a protected veteran, status as an individual with a disability, or other applicable legally protected characteristics. We also consider qualified applicants with criminal histories, consistent with applicable federal, state and local law. Meta participates in the E-Verify program in certain locations, as required by law. Please note that Meta may leverage artificial intelligence and machine learning technologies in connection with applications for employment.

"""
prompt_template = """
Read the instruction carefully based only on the following context:
{context}
 - -
Write a cover letter based on the above context: {question}
"""

embedding = embeddings()
llm = localllm()
text_splitter = text_splitter_semantic(job_desc, embedding)

save_data_vdb = save_to_chroma(text_splitter, embedding, 'rah')

job_description = query_rag("rah", embedding, prompt_template, llm)


def generate_cover_letter_open_source(job_description, resume):
    name = 'Sohanur'
    address = "bronx, New York, 10462"
    email = "srahman06@manhattan.edu"
    phone = "(929) 412 6398"
    date = datetime.date.today()
    prompt = (f"Imagine you are a world-renowned career strategist with decades of experience in creating compelling resumes that have helped countless individuals land their dream jobs. Your expertise lies in crafting resumes that not only showcase a candidate's skills and experiences but also weave in their unique story in a way that resonates with leading employers across various industries. Your secret lies in your ability to humanize each resume, transforming it into a narrative that highlights the candidate’s journey, achievements, and aspirations.",
              f"Do the following steps: "
              f"1. Read the following job description, like job titles, company name, responsiblity culture etc"
              f"2. Read the following resume, "
              f"3. Write a formal cover letter to the hiring manager for the job description based on the given resume and have 4 praragraph describing like a intro with job title and rusme person, 2 other paragraph the experience related to the resume and job description, last one make it why the company might be very interested to me based on the given info about the company, "
              # f"4. The cover letter MUST BE within {output_size_range[0]} to {output_size_range[1]} words. "
              # f"4. The cover letter MUST BE within 100 words. "
              f"4. Return ONLY the cover letter ONCE, and name {name}, {address}, {email}, {phone}, {date} this information at the top, nothing else"
              f"Job Description is given as dictionary or json format: '{job_description}'. Resume is text format: '{resume}'")

    # prompt = "What is an LLM"

    llm = ChatOllama(
        model="llama3.2:3b",
        temperature=0,
        # other params...
        )

    llm_response = llm.invoke(prompt)

    return llm_response

resume = extract_data("Rahman.pdf")

print(generate_cover_letter_open_source(job_description, resume).content)