from flask import Flask, request, session, Response
from twilio.twiml.messaging_response import MessagingResponse
# from bot import ask, append_interaction_to_chat_log

from dotenv import load_dotenv
from random import choice
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = "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"
completion = openai.Completion()



# @app.route('/bot', methods=['POST'])
# def bot():
#     incoming_msg = request.values['Body']
    
#     if "Main Menu" in incoming_msg or "menu" in incoming_msg or "main menu" in incoming_msg:
#         answer = '''
#             Welcome, Athenabot is here to help 1 million women entrepreneurs start and grow their technology businesses! Whether you're just starting out or looking to take your business to the next level, we've got you covered \n
#             1: Learn 📚
#             2: Ask a question 🙋🏻‍♀️
#         '''
#         msg = MessagingResponse()
#         msg.message(answer)
#         print(answer)
#         print(msg)
    
#         return str(msg)
    
#     if "purpose" in incoming_msg.lower():
#         answer = '''
#             Our Purpose, Who are we = "Building a technology startup can be an exciting and rewarding journey. 
#             As a woman looking to convert your business idea into a technology business, 
#             it's essential to have a clear roadmap to guide you along the way. 
#             Here's our guide to help you build a technology startup 🏗️💻🚀
#         '''
#         msg = MessagingResponse()
#         msg.message(answer)
#         print(answer)
#         print(msg)
    
#         return str(msg)
    
#     if "go back home" in incoming_msg.lower():
#         answer = '''
#             Welcome, Athenabot is here to help 1 million women entrepreneurs start and grow their technology businesses! Whether you're just starting out or looking to take your business to the next level, we've got you covered \n
#             1: Learn 📚
#             2: Ask a question 🙋🏻‍♀️
#         '''
#         msg = MessagingResponse()
#         msg.message(answer)
#         print(answer)
#         print(msg)
    
#         return str(msg)
    
#     if "go back home" == incoming_msg.lower():
#         answer = '''
#             Welcome, Athenabot is here to help 1 million women entrepreneurs start and grow their technology businesses! Whether you're just starting out or looking to take your business to the next level, we've got you covered \n
#             1: Learn 📚
#             2: Ask a question 🙋🏻‍♀️
#         '''
#         msg = MessagingResponse()
#         msg.message(answer)
#         print(answer)
#         print(msg)
    
#         return str(msg)
    
#     if "topic sequence" == incoming_msg.lower() or "what is topic sequence" == incoming_msg.lower():
#         answer = '''
#             - Topic Sequences \n
#             - Objectives \n
#             - Content \n
#             - Essential Essential Questions \n
#             - Identify a problem to solve\n
#             - Resources \n
#         '''
#         msg = MessagingResponse()
#         msg.message(answer)
#         print(answer)
#         print(msg)
    
#         return str(msg)

#     if "1" == incoming_msg.lower() or "Option 1" in incoming_msg.lower():
#         answer = '''
#             You Can Choose a Topic Below 
#             Topic 1 - Idea Validation
#             Topic 2 - Business Planning
#             Topic 3 - Product Development
#             Topic 4 - User Acquisition
#             Topic 5 - Funding and Finance
#             Topic 6 - Growth and Scaling
#         '''
#         msg = MessagingResponse()
#         msg.message(answer)
#         print(answer)
#         print(msg)
    
#         return str(msg)
    
#     chat_log = session.get('chat_log')
#     answer = ask(incoming_msg, chat_log)
#     # session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
#                                                         #  chat_log)
#     msg = MessagingResponse()
#     msg.message(answer)
#     print(answer)
#     print(msg)
   
#     return str(msg)

# if __name__ == '__main__':
#     app.run(debug=True)

import requests
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = '8wLs1T3BlbkFJUJ5BxAcvjbvkjgffvrOjUcAMX7njo78'


menu_options = {
    '1': {
        'name': 'Learn',
        'topics': [
            {
                'name': 'Idea Validation',
                'objectives': 
                    """ 
                        Objectives: \n
                        To learn how to validate a business idea by engaging with potential customers. 📈👥💭 \n
                        To identify a viable market and determine if there is a demand for the proposed product or service. 🌍🔍💰 \n
                        To identify potential challenges or obstacles to success and develop strategies for addressing them. 🤔👷📝 \n
                        
                        Send the word continue to proceed
                    """,
                'Essential Questions': ''' Essential Questions: \n What are the most effective questions to ask potential customers when validating a business idea? 🤔💭👥 \n
                How can you determine if a potential customer's feedback is valuable in the idea validation process? 🕵️‍♀️🔍💡 \n
                What are some common mistakes that entrepreneurs make when validating their business ideas? 💼💥🚫 \n
                Send the word continue to proceed
                ''',
                'content': '''
                    Content: \n
                    Introduction: Start by brainstorming your business idea and mapping out a clear plan of action. Conduct research to validate your idea and ensure that there's a market for it. 💡🧠
                    Identify a problem to solve: Start by identifying a problem that you are passionate about solving. Look for gaps in the market or challenges that you have personally experienced. Sample tool: Gap analysis template from Smartsheet (https://www.smartsheet.com/gap-analysis-template) 🔍💡👥💪
                    Identify your target audience and their needs: Determine who your target customers are, what their pain points are, and how your product or service can solve their problems. How to Validate Your Business Idea: https://www.entrepreneur.com/article/297899 🎯👥💡🔑
                    Research the market: Once you have identified a problem and target audience, research the market to determine if there is a demand for a solution. Use tools like Google Trends, industry reports, and customer surveys to gather data. Sample tool: Guide to Market Research: https://www.inc.com/guides/2010/06/conducting-market-research.html SurveyMonkey for creating surveys to collect market data (https://www.surveymonkey.com/) 📈🌍📊📝
                    Refine your idea: Based on your research, refine your idea and determine the unique value proposition that your product or service offers. Think about what sets you apart from competitors and write it down. 💡🔎✍️💎
                    \n
                    Send the word continue to proceed
                ''',
                'resources': 'Resources \n Read "The Mom Test" by Rob Fitzpatrick to learn how to effectively validate your business idea. 📖💡🤔\nWatch "How to Validate Your Startup Idea" by Y Combinator on YouTube - https://www.youtube.com/watch?v=CGlGp-B6oM8 📹💻👀 \n Send the word continue to proceed',
                'Assignment': ''' Assignment \n Conduct customer interviews to gather feedback on your business idea. Develop a list of potential customers and interview them to gather information about their pain points, needs, and preferences. 🗣️💬👥📝 \n Send the word continue to proceed '''
            },
            {
                'name': 'Business Planning',
                'objectives': 
                    """ 
                        Objectives: \n
                        To create a business plan that outlines the company's vision, mission, and objectives. 📝👀🌟
                        To identify the target market, competitors, and unique selling proposition of the business. 🎯👥🔍
                        To develop a marketing plan, sales strategy, and financial projections for the business. 📈💰📣 \n

                        Send the word continue to proceed
                    """,
                'Essential Questions': ''' Essential Questions \n How can you identify a problem that your business can solve? 🤔💭💡
                    What are the key components of a successful business plan? 📝🌟🔑
                    What financial metrics should you track in your business plan? 💰📊👀
                    \n
                    Send the word continue to proceed
                ''',
                'content': '''
                    Content: \n
                    
                    Introduction: After validating your business idea, it's time to start developing a solid business plan. This includes outlining your business model, revenue streams, and marketing strategy. 🚀💼🌟
                    \n
                    
                    Step 1: Define your business idea and mission 🌟💼🎯
                    To create a successful business plan, you need to start with a clear idea of what your business is and what you want to achieve. Here are some steps to follow: 📝👀🚀
                    Define your business idea: This includes identifying your target market, your products or services, and your unique selling proposition. Use a tool like the Business Model Canvas (https://strategyzer.com/canvas/business-model-canvas) to help you map out your business idea. 🎯💼🌟
                    Develop your mission statement: Your mission statement should define the purpose and values of your business. Use this guide from HubSpot (https://blog.hubspot.com/marketing/how-to-write-mission-statement) to help you craft a clear and concise mission statement. 📝👀🚀


                    Step 2: Conduct market research 📊
                    Before you launch your business, you need to understand your target market and competition. Here are some steps to follow:
                    Identify your target market 🎯: This includes understanding the demographics, needs, and behaviors of your ideal customers. Use tools like SurveyMonkey (https://www.surveymonkey.com/) or Google Forms (https://www.google.com/forms/about/) to create surveys and gather data. 📋
                    Research your competition 🔍: Look at other businesses in your industry or market to understand their strengths and weaknesses, pricing, and marketing strategies. 💼
                    Step 3: Develop your business strategy
                    Once you have a clear idea of your business and market, you need to develop a strategy to achieve your goals. Here are some steps to follow:
                    Define your goals: 🎯📈 This includes setting specific, measurable, and achievable goals for your business. Use the SMART goals framework (https://www.smartsheet.com/blog/essential-guide-writing-smart-goals) to help you set effective goals.
                    Develop your marketing strategy: 📣🤝 This includes identifying your target audience, creating a marketing budget, and selecting the most effective marketing channels for your business. Use this guide from HubSpot (https://blog.hubspot.com/marketing/marketing-strategy) to help you develop your marketing strategy.
                    Create your financial projections: 💰📊 This includes forecasting your revenue, expenses, and cash flow for the next few years. Use a financial forecasting tool like LivePlan (https://www.liveplan.com/) or QuickBooks (https://quickbooks.intuit.com/) to create your projections.
                    Analyze the competition: 🔎👀 Research the competition to determine what they are doing well and what opportunities exist for your business. Use tools like SEMrush and SimilarWeb to gather data. Sample tool: SWOT analysis template from MindTools (https://www.mindtools.com/pages/article/newTMC_05.htm)


                    Step 4: Write your business plan
                    Once you have a clear business strategy, you can start putting your business plan together. The business plan should contain the following section


                    Executive Summary: This section provides a brief overview of your business plan, including your business idea, target market, financial projections, and goals. Keep it concise and compelling. 💼💡💰
                    Business Description: In this section, provide a detailed description of your business, including what products or services you will offer, who your target audience is, and what makes your business unique. You may also want to discuss your industry and market research. 📝🏢🔍
                    Market Analysis: Conduct market research to identify your target market and your competition. Use this information to analyze your strengths and weaknesses, and to identify opportunities and threats. You may also want to include a SWOT analysis. 📊🔎💪
                    Marketing and Sales: In this section, outline your marketing and sales strategy. Discuss how you plan to promote your business, attract customers, and build brand awareness. Identify your target customers and explain how you plan to reach them. You may want to include a marketing budget. 📈💰🎯
                    Products and Services: Describe in detail the products or services you will offer. Explain how they will benefit your target audience, and how they differ from your competitors. You may also want to discuss any intellectual property or patents you hold. 🛍️💡🤝
                    Operations: Describe how your business will operate on a day-to-day basis, including your processes for production, distribution, and customer service. Include any operational challenges you may face, and how you plan to address them. 📦🚚👩‍💼
                    Financial Projections: This section should include your financial projections for the next three to five years, including your income statement, balance sheet, and cash flow statement. You may also want to include a break-even analysis, as well as any assumptions you have made about your business. 💰📈📉
                    Funding: Discuss how much funding you will need to start and operate your business, and where you plan to get it from. You may also want to include a discussion of your funding sources, such as angel investors or venture capitalists. 💸🤝💰
                    Appendix: Finally, include any additional information that may be relevant to your business plan, such as resumes of key team members, letters of reference, and other supporting documents. 📑👨‍💼🔖

                    
                    \n
                    Send the word continue to proceed
                ''',
                'resources': '''Resources \n Take the course "How to Build a Startup" by Udacity - https://www.udacity.com/course/how-to-build-a-startup--ep245
                Watch "How to Write a Business Plan" by Business Insider on YouTube - https://www.youtube.com/watch?v=9XVfeAjv5rM
                Business Model Canvas: https://strategyzer.com/canvas/business-model-canvas
                How to Write a Mission Statement: https://blog.hubspot.com/marketing/how-to-write-mission-statement
                SurveyMonkey: https://www.surveymonkey.com/
                Google Forms: https://www.google.com/forms/about/
                SMART Goals Framework: https://www.smartsheet.com/blog/essential-guide-writing-smart-goals
                Marketing Strategy: https://blog.hubspot.com/marketing/marketing-strategy
                LivePlan: https://www.liveplan.com/
                QuickBooks: https://quickbooks.intuit.com/
                ''',
                'Assignment': ''' Assignment \n Develop a business plan for your technology startup. This should include a clear value proposition, revenue model, and marketing strategy. 💡💰📈 '''
            },
            {
                'name': 'Product Development',
                'objectives': 
                    """ 
                        Objectives: \n
                        To develop a minimum viable product (MVP) that meets the needs of the target market. 🔨💡💻
                        To test and validate the MVP with potential customers. 🧪👥✅
                        To refine and iterate on the product based on customer feedback. 🔁👂📈
                        \n
                        
                        Send the word continue to proceed
                    """,
                'Essential Questions': ''' Essential Questions: \n What are the most important considerations when developing a minimum viable product?
                    How can you test your MVP with potential customers?
                    What are some common pitfalls to avoid when developing an MVP?

                ''',
                'content': '''
                    
                    Introduction 🚀: Building a technology startup requires developing a minimum viable product (MVP) that meets the needs of your target market. This module focuses on the product development process. 💻👨‍💼💡

                    Content: \n
                    
                    Step 1: Identify customer needs and pain points
                    To develop a successful product, it's important to start by identifying customer needs and pain points. Here are some steps to follow:
                    Conduct market research: Use surveys, focus groups, and other research methods to gather information about your target customers and their needs. 📊🧑‍🔬📝
                    Identify pain points: Determine what problems your customers are facing and how your product can solve those problems. 😖🎯💡
                    Create customer personas: Develop a detailed profile of your ideal customer, including their age, gender, income, interests, and other relevant characteristics. 👥📈👤
                    Step 2: Generate and evaluate product ideas
                    Once you have a clear understanding of your customer needs and pain points, it's time to generate and evaluate product ideas. Here are some steps to follow:
                    Brainstorm ideas 🧠💡🌀: Gather a team and brainstorm potential product ideas that meet the needs and solve the pain points of your target customers.
                    Evaluate ideas 📈📊🤔: Use a product evaluation matrix to assess the feasibility, marketability, and profitability of each product idea. The matrix should include criteria such as cost, uniqueness, competition, and revenue potential.
                    Select the best idea 👍🎉💯: Choose the product idea that best meets your criteria and has the highest potential for success.
                    Step 3: Develop and Test a Prototype (MVP)
                    Creating a prototype or MVP (Minimum Viable Product) 🛠️ is an essential step in product development. It allows you to test your product idea and gather feedback before investing significant resources into building a fully functional product. Here is a detailed guide on how to create a prototype or MVP: 📝
                    Step A: Identify the core features
                    Once you have defined the problem and solution, identify the core features that your product needs to have. These are the essential features that will make your product viable and valuable. Focus on creating a prototype that includes these core features. 💡👀📝
                    Step B: Choose the right prototyping method
                    There are several prototyping methods you can use, depending on your product's complexity and your resources. Here are some popular prototyping methods:
                    Paper prototyping 📝🖋️👨‍🎨: This involves creating a basic sketch or drawing of your product idea on paper. It's a quick and low-cost way to test your idea and gather feedback.
                    Digital prototyping 💻📐🔍: This involves using digital tools like Figma, Sketch, or Adobe XD to create a mockup of your product idea. You can add more detail and interactivity than paper prototyping.
                    3D printing 🖨️👨‍🏭🔧: This is a method used for physical product prototyping, where a 3D printer is used to create a physical model of your product idea.


                    Step C: Build the prototype
                    🛠️👷📏 Depending on the prototyping method you choose, you can start building your prototype. Keep in mind that you don't need to create a perfect prototype; it should be functional enough to test your product idea and gather feedback. Here are some tips for building a prototype:
                    Start with the core features: Focus on building the essential features of your product first. 🔍💻💡
                    Use off-the-shelf components: To save time and money, use off-the-shelf components like hardware and software libraries. 💰💻📚
                    Get feedback: Test your prototype with your target audience and gather feedback to improve your product idea. 🙋‍♀️📈💬
                    Step D: Refine the prototype
                    🔬👨‍🔬💡 After testing your prototype, use the feedback you receive to refine your product idea. Make changes and improvements to your prototype, based on the feedback you receive. Keep iterating until you have a product that meets your target audience's needs and is viable.
                    🔁👨‍💼💻 Creating a prototype or MVP can be an iterative process, and it's essential to test and refine your product idea before investing significant resources into building a fully functional product.
                    🛠️🧰👷‍♀️ By following these steps, you can create a prototype that will help you test your product idea and gather valuable feedback.

                    \n
                    Send the word continue to proceed
                ''',
                'resources': '''Resources \n Read "The Lean Startup" by Eric Ries to learn about building and testing your MVP.
                Watch "How to Build a Minimum Viable Product" by Startup Grind on YouTube - https://www.youtube.com/watch?v=CGikAEGIo0w
                Bubble for building MVPs without code (https://bubble.io/)
                ''',
                'Assignment': ''' Assignment \n Develop a minimum viable product (MVP) for your technology startup. This should be a functional prototype that can be tested by potential customers. 🚀💡💻 '''
            },
            {
                'name': 'User Acquisition',
                'objectives': 
                    """ 
                        Objectives: \n
                        To develop and implement a user acquisition strategy that targets the ideal customer profile. 🎯
                        To optimize marketing channels and campaigns for maximum ROI. 💰
                        To measure and analyze key performance metrics to track the success of user acquisition efforts. 📊
                        \n
                        
                        Send the word continue to proceed
                    """,
                'Essential Questions': ''' Essential Questions: \n What are the most effective channels for acquiring new customers?
                How can you use analytics to measure the success of your marketing efforts?
                What are some common mistakes that startups make when acquiring new customers?
                \n
                Send the word continue to proceed
                ''',
                'content': '''
                    Introduction: User acquisition is a critical aspect of building a successful technology startup. 🚀👥📈 This module focuses on developing strategies for acquiring and retaining customers. 💻🤝🔍                
                    Content: \n

                    User acquisition is a critical aspect of building a successful startup. Without users, your product or service will not gain traction, and your business will ultimately fail. Here are some steps to help you acquire users:
                🚀💰🎯 Step 1: Develop a Launch Plan
                Before you start acquiring users, you need to have a plan in place. This plan should include your goals, target audience, marketing channels, and metrics for success. Use a launch plan template like the one from Buffer (https://buffer.com/library/startup-launch-checklist/) to help you get started.
                💵💰📈 Step 2: Determine User Acquisition Costs
                It's important to know how much it will cost to acquire each user. This will help you determine your marketing budget and make sure you're not spending more money than you're making. Use a customer acquisition cost calculator like the one from HubSpot (https://www.hubspot.com/cac-calculator) to help you determine your user acquisition costs.
                📣📧💻 Step 3: Decide the Right User Acquisition Channels
                There are many different user acquisition channels to choose from, such as social media, SEO, email marketing, and paid advertising. It's important to choose the channels that are most effective for your target audience and industry. Use a channel selection tool like the one from GrowHack (https://www.growhack.com/tools/user-acquisition-channels/) to help you decide which channels to focus on.
                Step 4: Create Marketing Materials 📝📊💻
                Once you've chosen your user acquisition channels, you need to create marketing materials that will help you attract and retain users. This includes optimizing your landing page, creating social media ads and posts, and sending targeted emails. Use a marketing tool like HubSpot (https://www.hubspot.com/) or Mailchimp (https://mailchimp.com/) to help you create and distribute your marketing materials.
                Step 5: Measure Your Results 📈📊📉
                Finally, it's important to measure your user acquisition results and make changes as needed. Use metrics like conversion rates, customer lifetime value, and retention rates to help you determine the effectiveness of your user acquisition efforts. Use an analytics tool like Google Analytics (https://analytics.google.com/) or Mixpanel (https://mixpanel.com/) to help you track and analyze your user acquisition data.

                    \n
                    Send the word continue to proceed
                ''',
                'resources': '''Resources \n Take the course "Marketing in a Digital World" by the University of Illinois on Coursera - https://www.coursera.org/learn/marketing-digital
                Watch "How to Acquire Your First 100 Customers" by Alex Schultz on YouTube - https://www.youtube.com/watch?v=n_yHZ_vKjno
                Buffer Startup Launch Checklist: https://buffer.com/library/startup-launch-checklist/
                HubSpot Customer Acquisition Cost Calculator: https://www.hubspot.com/cac-calculator
                GrowHack User Acquisition Channel Selection Tool: https://www.growhack.com/tools/user-acquisition-channels/
                HubSpot Marketing Tool: https://www.hubspot.com/
                Mailchimp: https://mailchimp.com/
                Google Analytics: https://analytics.google.com/
                Mixpanel: https://mixpanel.com/
                ''',
                'Assignment': ''' Assignment \n Develop a user acquisition strategy for your technology startup. This should include a plan for acquiring and retaining customers, as well as metrics for measuring success. 🚀🎯💻 '''
            },
            {
                'name': 'Funding and Finance',
                'objectives': 
                    """ 
                        Objectives: \n
                        To learn about the different types of funding available to startups 🤝.
                        To develop a compelling pitch to potential investors and secure funding for the business 💰.
                        To manage the finances of the business and track key financial metrics to ensure profitability and growth 📊.
                        \n
                                                
                        Send the word continue to proceed
                    """,
                'Essential Questions': ''' Essential Questions: \n 🤑 What are the different types of funding available to startups?
                👨‍💼 How can you create a compelling pitch to potential investors?
                💰 What financial metrics are most important to track when raising capital?
                \n
                Send the word continue to proceed
                ''',
                'content': '''
                    Content: \n
                    
                    Introduction: Funding is essential for scaling your technology startup. This module focuses on developing a funding strategy and understanding finance.
                    🚀💰💻 Step 1: Determine your startup costs and financial projections
                    To start, it's important to determine your startup costs and create financial projections for your business. This will help you understand how much funding you will need and how you plan to spend that funding. Here are some steps to follow:
                    💡 Estimate your startup costs: This includes everything from equipment and supplies to legal and administrative fees. Use a startup cost calculator like the one from Entrepreneur (https://www.entrepreneur.com/calculators/startupcosts) to get an estimate.
                    📈 Create a financial forecast: This should include your projected revenue, expenses, and cash flow for the first few years of your business. Use a financial forecasting tool like LivePlan (https://www.liveplan.com/) or QuickBooks (https://quickbooks.intuit.com/) to create your forecast.
                    💰 Determine your funding needs: Based on your startup costs and financial forecast, determine how much funding you will need to get your business off the ground and keep it running until it becomes profitable.
                    Step 2: Explore funding options
                    Once you know how much funding you need, it's time to explore your funding options. Here are some steps to follow:
                    Research grants and loans: Look for grants and loans that are specific to women entrepreneurs, such as those offered by the National Association of Women Business Owners (https://www.nawbo.org/resources/grants). 💰💸💰
                    Consider crowdfunding: Crowdfunding platforms like Kickstarter (https://www.kickstarter.com/) and Indiegogo (https://www.indiegogo.com/) allow you to raise money from a large number of people who believe in your business idea. 🤑🙌🏼🚀
                    Explore venture capital: Venture capital firms can provide large amounts of funding in exchange for equity in your company. Look for firms that focus on investing in women-led startups, such as Female Founders Fund (https://femalefoundersfund.com/). 💼💵💪
                    Step 3: Prepare your pitch
                    To secure funding, you'll need to pitch your business idea to investors. Here are some steps to follow:
                    Develop a pitch deck: A pitch deck is a visual presentation that outlines your business idea, market opportunity, and financial projections. Use a pitch deck template like the one from Canva 🎨 (https://www.canva.com/templates/presentations/MABRY_LHX-w-investor-pitch-deck/) to create your own.
                    Practice your pitch: Practice delivering your pitch to friends, family, or mentors to get feedback and refine your message. 🗣️💬
                    Network with investors: Attend events and join online communities to connect with potential investors who are interested in your industry or type of business. 🤝💼💰
                    \n
                    Send the word continue to proceed
                ''',
                'resources': '''Resources \n The Ultimate Guide to Startup Costs: https://www.entrepreneur.com/article/243919
                LivePlan: https://www.liveplan.com/
                QuickBooks: https://quickbooks.intuit.com/
                Grants and Funding Resources for Women Entrepreneurs: https://www.nawbo.org/resources/grants
                Kickstarter: https://www.kickstarter.com/
                Indiegogo: https://www.indiegogo.com/
                Female Founders Fund: https://femalefoundersfund.com/
                Pitch Deck Template from Canva: https://www.canva.com/templates/presentations/MABRY_LHX-w-investor-pitch-deck/
                Take the course "Entrepreneurship and Family Business" by the University of Pennsylvania on Coursera - https://www.coursera.org/learn/entrepreneurship-family-business
                Watch "How to Raise Money for Your Startup" by Patrick Bet-David on YouTube - https://www.youtube.com/watch?v=3bzLmtV8oOY
                \n Send the word continue to proceed''',
                'Assignment': ''' Assignment \n Develop a 💰 funding strategy for your 🚀 technology startup. This should include a plan for 📈 raising capital, as well as a 💵 financial plan for managing your startup. '''
            },
            {
                'name': 'Growth and Scaling',
                'objectives': 
                    """ 
                        Objectives: \n
                        To develop a growth strategy that leverages network effects and expands the customer base. 🌱📈💼
                        To identify and address potential scalability issues and develop strategies for scaling the business. 🤔📉🚀
                        To track and measure key performance metrics to ensure the continued success of the business. 📊💹✅
                        \n
                        
                        Send the word continue to proceed
                    """,
                'Essential Questions': ''' Essential Questions: \n How can you leverage network effects to accelerate growth? 📈🌐💥
                    What are the most important metrics to track when scaling your startup? 📊📈💻
                    What are some common challenges that startups face when scaling their businesses? 🤔📉💼
                 \n
                Send the word continue to proceed
                ''',
                'content': '''

                    🌱💹🚀 Introduction: Once your technology startup has secured funding and has a solid user acquisition strategy, it's time to focus on growth and scaling. This module focuses on developing a growth strategy and scaling your startup.
                    
                    \n 
                    
                    Content: \n
                    
                    Step 1: Evaluate your business growth potential
                    The first step to growing and scaling your business is to evaluate its potential for growth. Here are some steps to follow:
                    🔍💰👥 Assess your current position: Take a step back and evaluate where your business currently stands. This includes looking at your financials, customer base, and market position.
                    🌐📈 Evaluate your market: Look at the size and growth potential of your market to determine if there is room for your business to grow. Use market research tools like Statista (https://www.statista.com/) or IBISWorld (https://www.ibisworld.com/) to help with your evaluation.
                    🔍🆚📊 Analyze your competition: Look at your competition to see how they are currently operating and identify areas where your business can differentiate itself.
                    Step 2: Develop a growth strategy
                    Once you have evaluated your business's growth potential, it's time to develop a growth strategy. Here are some steps to follow:
                    Identify growth opportunities 🌱🔍: Based on your evaluation, identify areas where your business can grow. This could include expanding into new markets or product lines, increasing marketing efforts, or improving operations.
                    Set growth goals 📈🎯: Develop specific and measurable goals for your business's growth. This could include revenue targets, customer acquisition goals, or other metrics that align with your growth opportunities.
                    Create a growth plan 📝🚀: Develop a plan that outlines how you will achieve your growth goals. This could include hiring additional staff, investing in marketing or technology, or developing strategic partnerships.
                    Step 3: Secure funding for growth
                    To fund your growth plan, you may need to secure additional funding. Here are some steps to follow:
                    Explore funding options: 🔍💰 Look into funding options like venture capital, bank loans, or crowdfunding. Be sure to research funding options that are specific to your business type or industry.
                    Prepare your pitch: 🗣️📈 Develop a pitch that outlines your business's growth potential, goals, and plan. Use a pitch deck template like the one from Canva (https://www.canva.com/templates/presentations/MABRY_LHX-w-investor-pitch-deck/) to create your own.
                    Connect with investors: 🤝👥 Attend events and join online communities to connect with potential investors who are interested in your industry or type of business.


                    \n
                    Send the word continue to proceed
                ''',
                'resources': '''Resources \n Statista: https://www.statista.com/
                IBISWorld: https://www.ibisworld.com/
                Pitch Deck Template from Canva: https://www.canva.com/templates/presentations/MABRY_LHX-w-investor-pitch-deck/
                Read "Zero to One" by Peter Thiel to learn about developing a growth strategy.
                Watch "How to Scale a Startup" by Startup Grind on YouTube - https://www.youtube.com/watch?v=TwaJqoqNbIA
                \n Send the word continue to proceed''',
                'Assignment': ''' Assignment \n Develop a growth strategy for your technology startup. This should include a plan for scaling your business, as well as metrics for measuring success. 📈📊 '''
            }
        ]
    },
    '2': {
        'name': 'Ask a Question',
        'topics': []
    }
}

start_sequence = "\nBot:"
restart_sequence = "\n\nPerson:"
session_prompt = """

I am athenabot, My name is athenabot.
__

Our Purpose, Who are we = "Building a technology startup can be an exciting and rewarding journey. 
As a woman looking to convert your business idea into a technology business, 
it's essential to have a clear roadmap to guide you along the way. 
Here's our guide to help you build a technology startup 🏗️💻🚀"

__

Topic 1: Idea Validation

Objectives "To learn how to validate a business idea by engaging with potential customers. 📈👥💭
To identify a viable market and determine if there is a demand for the proposed product or service. 🌍🔍💰
To identify potential challenges or obstacles to success and develop strategies for addressing them. 🤔👷📝"

Continue or go back home


Topic 2: Business Planning
Objectives:




Step 1: Define your business idea and mission 🌟💼🎯
To create a successful business plan, you need to start with a clear idea of what your business is and what you want to achieve. Here are some steps to follow: 📝👀🚀
Define your business idea: This includes identifying your target market, your products or services, and your unique selling proposition. Use a tool like the Business Model Canvas (https://strategyzer.com/canvas/business-model-canvas) to help you map out your business idea. 🎯💼🌟
Develop your mission statement: Your mission statement should define the purpose and values of your business. Use this guide from HubSpot (https://blog.hubspot.com/marketing/how-to-write-mission-statement) to help you craft a clear and concise mission statement. 📝👀🚀


Step 2: Conduct market research 📊
u
Essential Questions:


What are the most important considerations when developing a minimum viable product?
How can you test your MVP with potential customers?
What are some common pitfalls to avoid when developing an MVP?



Introduction 🚀: Building a technology startup requires developing a minimum viable product (MVP) that meets the needs of your target market. This module focuses on the product development process. 💻👨‍💼💡
Content:
Step 1: Identify customer needs and pain points
To develop a successful product, it's important to start by identifying customer needs and pain points. Here are some steps to follow:
Conduct market research: Use surveys, focus groups, and other research methods to gather information about your target customers and their needs. 📊🧑‍🔬📝


Step C: Build the prototype
🛠️👷📏 Depending on the prototyping method you choose, you can start building your prototype. Keep in mind that you don't need to create a perfect prototype; it should be functional enough to test your product idea and gather feedback. Here are some tips for building a prototype:


Resources:
Read "The Lean Startup" by Eric Ries to learn about building and testing your MVP.
Watch "How to Build a Minimum Viable Product" by Startup Grind on YouTube - https://www.youtube.com/watch?v=CGikAEGIo0w
Bubble for building MVPs without code (https://bubble.io/)


📝 Assignment: Develop a minimum viable product (MVP) for your technology startup. This should be a functional prototype that can be tested by potential customers. 🚀💡💻
Topic 4: User Acquisition

Objectives:


To develop and implement a user acquisition strategy that targets the ideal customer profile. 🎯
To optimize marketing channels and campaigns for maximum ROI. 💰
To measure and analyze key performance metrics to track the success of user acquisition efforts. 📊


Essential Questions:


What are the most effective channels for acquiring new customers?
How can you use analytics to measure the success of your marketing efforts?
What are some common mistakes that startups make when acquiring new customers?


Introduction: User acquisition is a critical aspect of building a successful technology startup. 🚀👥📈 This module focuses on developing strategies for acquiring and retaining customers. 💻🤝🔍
Content:
User acquisition is a critical aspect of building a successful startup. Without users, your product or service will not gain traction, and your business will ultimately fail. Here are some steps to help you acquire users:
🚀💰🎯 Step 1: Develop a Launch Plan


Resources:
Take the course "Marketing in a Digital World" by the University of Illinois on Coursera - https://www.coursera.org/learn/marketing-digital
Watch "How to Acquire Your First 100 Customers" by Alex Schultz on YouTube - https://www.youtube.com/watch?v=n_yHZ_vKjno


📝 Assignment: Develop a user acquisition strategy for your technology startup. This should include a plan for acquiring and retaining customers, as well as metrics for measuring success. 🚀🎯💻
Topic 5: Funding and Finance

Objectives:


To learn about the different types of funding available to startups 🤝.
To develop a compelling pitch to potential investors and secure funding for the business 💰.
To manage the finances of the business and track key financial metrics to ensure profitability and growth 📊.


Essential Questions:


🤑 What are the different types of funding available to startups?
👨‍💼 How can you create a compelling pitch to potential investors?
💰 What financial metrics are most important to track when raising capital?
Introduction: Funding is essential for scaling your technology startup. This module focuses on developing a funding strategy and understanding finance.




Objectives:


To develop a growth strategy that leverages network effects and expands the customer base. 🌱📈💼
To identify and address potential scalability issues and develop strategies for scaling the business. 🤔📉🚀
To track and measure key performance metrics to ensure the continued success of the business. 📊💹✅


Essential Questions:


How can you leverage network effects to accelerate growth? 📈🌐💥
What are the most important metrics to track when scaling your startup? 📊📈💻
What are some common challenges that startups face when scaling their businesses? 🤔📉💼


🌱💹🚀 Introduction: Once your technology startup has secured funding and has a solid user acquisition strategy, it's time to focus on growth and scaling. This module focuses on developing a growth strategy and scaling your startup.
Content:
Step 1: Evaluate your business growth potential
The first step to growing and scaling your business is to evaluate its potential for growth. Here are some steps to follow:


"""

@app.route("/bot", methods=['POST'])
def bot():
    incoming_msg = request.values['Body'].lower()
    
    if 'menu' in incoming_msg or 'main menu' in incoming_msg:
        # Show menu options
        resp = MessagingResponse()
        
        resp.message('''Welcome, Athenabot is here to help 1 million women entrepreneurs start and grow their technology businesses! Whether you're just starting out or looking to take your business to the next level, we've got you covered \n 1: Learn 📚 \n 2: Ask a question 🙋🏻‍♀️''')
    
    
        return str(resp)
        
    elif incoming_msg == '1':
        # Show topics for Learn
        resp = MessagingResponse()
        
        resp.message('''
            You Can Choose a Topic Below \n 1. Idea Validation \n 2. Business Planning \n 3. Product Development \n 4. User Acquisition \n 5. Funding and Finance \n 6. Growth and Scaling             
        ''')
        # for i, topic in enumerate(menu_options['1']['topics']):
        #     resp.message(f'{i+1}. {topic["name"]}')
        session['current_topic'] = None
        return str(resp)
    
    elif incoming_msg == '2':
        # Show topics for Questions
        resp = MessagingResponse()
        resp.message("Ask Any Question!")
        return str(resp)
      
    elif incoming_msg in ['1.1', '1.2', '1.3', '1.4', '1.5', '1.6']:
        # Show topic content
        resp = MessagingResponse()
        
        topic_num = int(incoming_msg.split('.')[1]) - 1
        topic = menu_options['1']['topics'][topic_num]
        
        # resp.message(f'{topic["name"]}:\n{topic["objectives"]}\n\n{topic["content"]}\n\nResources:\n{topic["resources"]}')
        resp.message(f'{topic["name"]}:\n')
        resp.message('Say "continue" to see the next section.')
        
        session['current_topic'] = topic_num
        session['current_section'] = 0
        return str(resp)
        
        
    elif incoming_msg == 'continue':
        resp = MessagingResponse()
        
        # Show next section
        
        if 'current_topic' not in session:
            resp.message('Please choose a topic first.')
            return str(resp)

        current_topic = session['current_topic']
        current_section = session.get('current_section', 0)
        topic = menu_options['1']['topics'][current_topic]
        sections = [topic['objectives'], topic['Essential Questions'], topic['content'], topic['resources'], topic['Assignment']]
        if current_section == len(sections):
            # If all sections have been shown, reset session and return to topic selection
            session.pop('current_topic', None)
            session.pop('current_section', None)
            resp.message('You have reached the end of this topic. Please choose another topic to learn about.')
            return str(resp)
        else:
            # Show the next section
            resp.message(sections[current_section])
            session['current_section'] = current_section + 1
            return str(resp)
    else:
        prompt_text = f'{session_prompt}{restart_sequence}: {incoming_msg}{start_sequence}:'
        resp = MessagingResponse()
        
        response = openai.Completion.create(
            engine="text-davinci-003",
            # model="text-davinci-003",
            prompt=prompt_text,
            temperature=0.7,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.3,
            stop=["\n"],
        )
        
        resp.message(response['choices'][0]['text'])

        return str(resp)
    

if __name__ == '__main__':
    app.run(debug=True)