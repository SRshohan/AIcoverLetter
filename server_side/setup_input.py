import fitz
from fpdf import FPDF
import os

def generate_pdf(filled_cover_letter):
    # Generate PDF using FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=12)

    # Split the filled cover letter into lines and add to PDF
    for line in filled_cover_letter.split('\n'):
        pdf.cell(200, 10, txt=line, ln=True)

def extract_data(pdf_file):
    # Prepare the data for the template
    if os.path.exists(pdf_file):
        doc = fitz.open(pdf_file)
        text = ""
        for page in doc:
            text+=page.get_text()
        print(text)
        return text
    else:
        print("File doesnt exists!")

def job_description():
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
    return job_desc