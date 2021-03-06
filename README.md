# CSCI 365 - Computational Finance Final Project

### Overview <br/>
The goal of the final project is to reinforce what you have learned in class and give you a chance to implement
some of the pricing models we had discussed in class. The project will be done in a group of 3 students. At
the end of the semester, one of the member will have to pack all the files into a single zip file and email that
zip file to me with a subject of CF_Final_Project. The unzipped files will be in a folder with the name of your
group. The package should include the following.<br/>
A. A single Microsoft Word or PDF that summarize all of the findings and answers to the questions I asked
below.<br/>
B. All the corresponding python files along with any data files.<br/>
C. A single Jupyter notebook with corresponding results. I should not need to re-run your notebook. But if
I do choose to re-run your notebook, it should run through without any errors. I will upload the Jupyter
notebook template on Blackboard.<br/>


![This is an image](https://images.mktw.net/im-473176?width=700&height=482)

## Components of the project
There are two major parts of the project. The first is to use technical as well as fundamental analysis to come
up with two buy and sell recommendations among a given set of 30 stocks. One recommendation will be
based on technical analysis and the other will be based on fundamental analysis. The second part of the
project is to implement a binomial as well as a Black-Scholes model for pricing options. <br/>
Milestone and code templates of the project <br/>
In order to avoid the situation where only one member does most of the work or none of the members start
working on the project until the very last min, I require each group to check off each milestones on the class
final project google sheet as we progress through the semester. I will upload code templates to help you
acheive the goal of the projects. You can deviate from the code template and fix whatever you think is
needed. However, I do not see the reason for your final codes to be dramatically different. <br/>
### Milestone 1 <br/>
A. Form your team. Start knowing your team members. <br/>
### Milestone 2 <br/>
A. Find the "EPS next 5Y" field from finviz.com. Add that in the StockUniverse.csv file. <br/>
B. Fill in the missing code in download_fundamental_data.py implementation. Run it to generate a
StockUniverseWithData.csv output file. <br/>
### Milestone 3 <br/>
A. Fill in the missing code in the stock.py
CFFinalProject.md 6/17/2021 
2 / 2 <br/>
B. Fill in the missing code in the discount_cf_model.py <br/>
C. Fill in the missing code in run_DCF.py. Run it to generate a StockUniverseValuation.csv file. <br/>
### Milestone 4 <br/>
A. Fill in the missing code in the binomial_model.py <br/>
B. Fill in the missing code in the BlackScholes_model.py <br/>
### Milestone 5 <br/>
A. Write a summary report what your group's buy and sell recommendation is. It should have date of the
analysis and brief description the reasoning behind. One recommendation should be based on
technical analysis. The other should be based on fundamental analysis. For technical analysis, include a
screen shot of the technical indicators that you used. <br/>
B. Download the Final Project Jupyter notebook. Answer the questions. 
Checklist of the files included in the zip file <br/>
A. A summary in Word or pdf <br/>
B. StockUniverse.csv <br/>
C. StockUniverseWithData.csv <br/>
D. StockUniverseValuation.csv <br/>
E. utils.py, download_fundamental_data.py, stock.py, discount_cf_model.py, run_DCF.py,
binomial_model.py, BlackScholes_model.py <br/>
F. FinalPoject Jupyter notebook. <br/>
