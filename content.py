"""
Site content — everything the pages render, in one place.

Two identities share a person: the accent colour, copy, experience framing and
project set all swap between them. Facts stay constant; only emphasis moves.
Source of truth for experience wording is the canonical resume set in
~/Desktop/Simon Job Search 2026/01 Base Resumes/00 Canonical Bases.
"""

BASE = "/Users/7ang/Desktop/Github Academic Project"

SHARED = dict(
    name="Simon Chen",
    email="xingyang@marshall.usc.edu",
    phone="(949) 591-3777",
    location="Los Angeles, CA",
    linkedin="https://www.linkedin.com/in/simonxy-chen",
    github="https://github.com/Semin1c",
    education=[
        dict(school="University of Southern California, Marshall School of Business",
             place="Los Angeles, CA", date="May 2026",
             degree="Master of Science in Business Analytics (STEM)",
             note="GPA 3.78 · Dean's Honor List, 3 semesters"),
        dict(school="University of California, Irvine", place="Irvine, CA", date="June 2024",
             degree="Bachelor of Arts in Business Economics, Minor in Management",
             note="GPA 3.92 · Dean's Honor List, 9 quarters · Phi Beta Kappa"),
    ],
)

MODES = {
"analyst": dict(
    key="analyst", label="Data / Business", accent="#990000", gold="#FFCC00",
    school="USC", eyebrow="Data &amp; Business Analytics",
    headline="Simon Chen",
    name_pre="Hi, I'm 『Xingyang』",
    role="Data Analyst &amp; Scientist",
    lede="A team-oriented analyst who values data and technology, but believes the real foundation "
         "is still human insight, judgment and interaction. Right now I'm finishing a Master's in "
         "Business Analytics at USC Marshall.",
    nav_tag="Data &amp; Business Analytics",

    about_title="Data is the tool. The judgment around it is the work.",
    about=[
        "My background is in business analytics and economics, and I'm especially interested in "
        "work across business, sports, performance and decision-making. I enjoy using data, "
        "visualization and new technology to make sense of problems and move toward better answers. "
        "But to me the work is never just about tools — it's also about communication, context, "
        "domain understanding, and knowing how to turn analysis into something useful in the real world.",
        "I don't see AI as an enemy, but as a partner — something to learn with, experiment with, "
        "and use alongside human perspective to build better insight and better decisions.",
        "The habit I've built along the way is checking my own work before anyone else has to. "
        "A retention programme I'd sized at a 13x return was worth closer to 1.2x once I costed it "
        "against real headcount. A model scoring well turned out to be answering a different question "
        "than the one we'd asked. Catching those myself matters more to me than the first number "
        "looking good.",
        "<span class='todo'>[Simon — your paragraph. What you're like outside this: what you watch, "
        "play, argue about. Brittany Chiang's version is \"climbing, playing tennis, hanging out with "
        "my wife and two cats, and running around Hyrule searching for Korok seeds.\" Specific beats "
        "impressive. This is the paragraph people remember.]</span>",
    ],
    about_kicker="What I bring",
    brings=[
        ("Structured problem solving",
         "Starting from the decision someone actually needs to make, then working back to what the "
         "data has to answer — rather than starting from whatever is in the file."),
        ("Data with context",
         "A number means little without knowing how it was collected, what it leaves out, and who "
         "is going to act on it. I spend as much time on that as on the modelling."),
        ("Communication that translates",
         "Most of the people who need an answer aren't analysts. Getting a finding across to a coach, "
         "a manager or a room that doesn't share your vocabulary is part of the job, not an extra."),
        ("Collaborative mindset",
         "I've worked inside performance teams and run projects across a 200+ member lab. The useful "
         "work almost always comes from the conversation, not from someone analysing alone."),
        ("Curiosity that keeps expanding",
         "Sports, business, performance, new tooling. I'd rather learn a new domain properly than "
         "stay in one lane, and most of what I've found interesting came from that."),
    ],
    about_list=[
        ("Churn and retention", "Who leaves, what actually drives it, and what keeping them is worth."),
        ("Pricing and risk", "Loss modelling on heavily skewed distributions where the average is useless."),
        ("BI and reporting", "Power BI dashboards with what-if scenarios that survive contact with a real budget."),
        ("Data pipelines", "Multi-source ingestion, ID matching, and validation that runs without babysitting."),
    ],

    xp_title="Where I've done this",
    experience=[
        dict(org="Excel Sports Management", date="Jun — Aug 2025",
             role="Sports Performance Associate, Analytics",
             prose="Built the pipeline the performance team ran on — five-plus sources and APIs pulled "
                   "together, cleaned, ID-matched and turned into reporting for 200+ athletes, which took "
                   "about 80% of the recurring work out. I also built the R Shiny and Streamlit tools they "
                   "kept using after I left, which I care about more than the percentage.",
             tags=["R", "Python", "APIs", "ETL", "R Shiny", "Streamlit"]),
        dict(org="Trojans Sports Research Lab", date="Jan 2025 — Present",
             role="Program & Project Manager",
             prose="I run analytics projects inside a 200+ member lab — five or more at a time, five to ten "
                   "people each. Most of the job is unglamorous: writing the data-collection standards, "
                   "building the templates, recording the tutorial so thirty-odd people stop asking the same "
                   "question. Getting that right is what makes the analysis possible.",
             tags=["Python", "SQL", "Data standards", "Project management"]),
        dict(org="China Merchants Securities", date="Apr — Aug 2023",
             role="Investment Banking Analyst Intern",
             prose="A summer in investment banking in Beijing. I went through 2020–2023 financials for eight "
                   "companies, then dug properly into two of them — subsidiary listings, and whether the "
                   "business, resource and capital synergies were actually there. I also rewrote parts of "
                   "two or three convertible-bond and refinancing proposals, which is where I learned how "
                   "much of finance is formatting.",
             tags=["Financial analysis", "Excel", "Valuation"]),
    ],

    writing_title="Things I've been working out",
    writing_lede="Findings from my own work, written as arguments rather than project pages. "
                 "Drafts in progress — the analysis is done, the writing isn't.",
    writing=[
        dict(title="How I talked myself out of a 13x return",
             desc="A retention programme priced against an industry benchmark looked like a money printer. "
                  "Priced against the actual headcount it was worth $83K. The arithmetic that makes the "
                  "difference is embarrassingly simple.",
             status="Draft"),
        dict(title="Your accuracy score is probably measuring your majority class",
             desc="I reported 88–90% accuracy on a classifier and felt good about it. The majority class "
                  "was 85.6%. What I'd actually built was barely better than answering the same way every time.",
             status="Draft"),
        dict(title="A metric can be right and still be useless",
             desc="A composite score reproduced its own specification perfectly, ranked listings sensibly, "
                  "and produced a city ranking where first place won by 0.005 points. Precision isn't signal.",
             status="Outline"),
        dict(title="What I got wrong in my first year of analytics",
             desc="Reading an interaction coefficient without its main effect. Trusting a target variable's "
                  "label. Three or four mistakes I made that nobody flagged, and how I caught them.",
             status="Idea"),
    ],

    proj_title="Three that show the range",
    proj_lede="Churn, workforce economics, and the dashboard that talked a budget out of being spent.",
    projects=[
        dict(tag="Churn · Streaming", title="Netflix Subscriber Churn",
             stat="5,000", label="subscribers modelled",
             desc="Engagement is the only driver that matters. Strip viewing behaviour out and three "
                  "different classifiers collapse to barely better than a coin flip.",
             body="Across 5,000 subscribers, how much someone watches separates churners from stayers "
                  "so cleanly that everything else is noise. The retention play targets disengaged "
                  "Basic-plan subscribers specifically, because that's where spend has somewhere to go.",
             fig=f"{BASE}/MKT 566 - Netflix Churn Prediction (2025 Fall)/Git Version/figures/churn_by_engagement.png",
             repo="https://github.com/Semin1c/netflix-churn-engagement", stack="Python · scikit-learn · XGBoost"),
        dict(tag="People analytics · ROI", title="Employee Attrition & Retention ROI",
             stat="0.85", label="held-out ROC-AUC",
             desc="Attrition concentrates hard enough that two segments cover a third of departures "
                  "across a tenth of the workforce. The honest ROI is a fraction of the headline one.",
             body="1,470 employees, 31 features, regularised logistic regression. Business travel, "
                  "overtime and promotion timing carry the signal. Turning risk scores into a "
                  "156-employee pilot covers 35% of predicted departures — and re-costing the programme "
                  "per employee and per role replaced a benchmark-driven 13x with a defensible $83K.",
             fig=f"{BASE}/DSO 550 - IBM Employee Attrition ROI (2026 Spring)/Git Version/outputs/figures/exec/step3_segment_playbook_onepager.png",
             repo="https://github.com/Semin1c/ibm-attrition-roi", stack="Python · scikit-learn · statsmodels"),
        dict(tag="BI · What-if modelling", title="Sales Performance Dashboards",
             stat="−15%", label="ROI on the training everyone wanted",
             desc="Three Power BI dashboards on a $25.7M book, tracing a question from \"how are we "
                  "doing\" to \"what should we fund\" — and finding the obvious answer loses money.",
             body="Training looks like a driver in a decomposition tree, so the instinct is to fund it. "
                  "Tested directly, rep attributes correlate near zero with sales per rep. What "
                  "separates reps is who they report to — a $134K supervisor gap. Both costings of the "
                  "training programme come back negative.",
             fig=f"{BASE}/DSO 550 - People Analytics Power BI Dashboards (2026 Spring)/Git Version/figures/what_actually_drives_sales.png",
             repo="https://github.com/Semin1c/people-analytics-dashboards", stack="Power BI · DAX · What-if parameters"),
    ],
    skills=[
        ("Analytics & modelling", "SQL · Python · R · Regression · Classification · Clustering · Forecasting · A/B testing"),
        ("BI & reporting", "Power BI · Tableau · R Shiny · Streamlit · Excel · KPI development"),
        ("Data & platforms", "PostgreSQL · ETL · APIs · Data modelling · Data quality · Git/GitHub"),
        ("Languages", "English and Chinese (bilingual) · Spanish (intermediate)"),
    ],
    contact_title="Open to analyst roles",
    contact_lede="Looking for data and business analyst positions, starting May 2026. "
                 "Email is the fastest way to reach me.",
),

"sports": dict(
    key="sports", label="Sports", accent="#0064A4", gold="#FFD200",
    school="UC Irvine", eyebrow="Sports Analytics",
    headline="Simon Chen",
    name_pre="Hi, I'm 『Xingyang』",
    role="Sports Analytics",
    lede="Two seasons inside sports performance and a Master's in Business Analytics at USC Marshall. "
         "I work on team and player questions, and I care as much about whether a finding is usable by "
         "a coach as whether it holds up statistically.",
    nav_tag="Sports Analytics",

    about_title="The data matters. So does knowing the game around it.",
    about=[
        "<span class='todo'>[Simon — the origin story. Why sports, and why you kept choosing it when "
        "the economics degree pointed somewhere else. Which teams, which moment made this stick. Two "
        "or three sentences, specific. This is the one a club will read twice.]</span>",
        "A lot of football analysis rests on claims nobody has actually checked — that possession wins "
        "matches, that the crowd drives home advantage, that Europe's big five out-compete MLS. Each of "
        "those is testable, and each one weakens or reverses when you run it properly. I find that more "
        "interesting than confirming what people already believe.",
        "That includes my own work. One project opened from an assumption printed on slide two of the "
        "deck, and I coded it straight into the target variable before going back and finding the data "
        "said the opposite. Admitting that is what made the project worth anything.",
        "Alongside the analysis, two seasons inside sports performance — building athlete pipelines, "
        "working on readiness monitoring, and making tools the coaching staff kept using after I left. "
        "That part taught me that a finding nobody can act on isn't finished.",
    ],
    about_kicker="What I bring",
    brings=[
        ("Structured problem solving",
         "Starting from the decision someone actually needs to make, then working back to what the "
         "data has to answer — rather than starting from whatever is in the file."),
        ("Data with context",
         "A number means little without knowing how it was collected, what it leaves out, and who "
         "is going to act on it. I spend as much time on that as on the modelling."),
        ("Communication that translates",
         "Most of the people who need an answer aren't analysts. Getting a finding across to a coach, "
         "a manager or a room that doesn't share your vocabulary is part of the job, not an extra."),
        ("Collaborative mindset",
         "I've worked inside performance teams and run projects across a 200+ member lab. The useful "
         "work almost always comes from the conversation, not from someone analysing alone."),
        ("Curiosity that keeps expanding",
         "Sports, business, performance, new tooling. I'd rather learn a new domain properly than "
         "stay in one lane, and most of what I've found interesting came from that."),
    ],
    about_list=[
        ("Match and season analysis", "Possession, chance creation, home advantage, competitive balance."),
        ("Player and roster evaluation", "What transfers across clubs, and what was only ever context."),
        ("Athlete performance data", "Workload, readiness and testing data turned into coach-facing tools."),
        ("Schedule and travel", "Rest, compression and opponent sequencing separated from team quality."),
    ],

    xp_title="Where I've done this",
    experience=[
        dict(org="Excel Sports Management", date="Jun — Aug 2025",
             role="Sports Performance Associate, Analytics",
             prose="A summer inside a performance team, modelling how neuromuscular, sprint, strength, "
                   "pitch-speed and bat-speed measures actually relate to each other, and building the "
                   "pipeline that fed three to ten athlete reviews a week for 200+ athletes. The R Shiny "
                   "and Streamlit dashboards I built are still in use, which is the part I'd point at.",
             tags=["R", "Python", "Athlete monitoring", "R Shiny", "Streamlit"]),
        dict(org="Trojans Sports Research Lab", date="Jan 2025 — Present",
             role="Program & Project Manager",
             prose="I manage sports research projects inside a 200+ member lab — five or more at a time, "
                   "five to ten people each, built around student schedules. Two of the projects I worked "
                   "on had abstracts accepted by ACSM, and I presented both posters on site.",
             tags=["Python", "SQL", "Research design", "ACSM"]),
        dict(org="China Merchants Securities", date="Apr — Aug 2023",
             role="Investment Banking Analyst Intern",
             prose="A summer in investment banking in Beijing, going through 2020–2023 financials for eight "
                   "companies and digging properly into two of them. Not sports, but it's where I learned to "
                   "be suspicious of a number before repeating it.",
             tags=["Financial analysis", "Excel", "Valuation"]),
    ],

    writing_title="Things I've been working out",
    writing_lede="Findings from my own work, written as arguments rather than project pages. "
                 "Drafts in progress — the analysis is done, the writing isn't.",
    writing=[
        dict(title="Possession is a bad KPI. Box touches are a better one.",
             desc="Across 160 Premier League squad-seasons, one variable beat the full 23-metric set on "
                  "clubs the model had never seen. Most of what we measure about possession is describing "
                  "the same thing twice.",
             status="Draft"),
        dict(title="MLS has more parity than the Premier League",
             desc="Two independent measures, fourteen seasons, and a result that reverses the thing "
                  "everybody says. Bayern won 11 of 14 Bundesliga titles over the same span.",
             status="Draft"),
        dict(title="Your accuracy score is probably measuring your majority class",
             desc="I reported 88–90% accuracy on a classifier and felt good about it. The majority class "
                  "was 85.6%. What I'd actually built was barely better than answering the same way every time.",
             status="Draft"),
        dict(title="The crowd isn't why home teams win",
             desc="Attendance predicts home points right up until you control for which clubs fill big "
                  "stadiums. Then it's nothing. The referees aren't it either.",
             status="Outline"),
    ],

    proj_title="Four findings that reversed the assumption",
    proj_lede="Possession, home advantage, competitive balance, and what a schedule is actually worth.",
    projects=[
        dict(tag="Premier League · 8 seasons", title="Possession vs. Box Entry",
             stat="23", label="metrics beaten by one",
             desc="Possession share explains almost nothing. Touches in the box explain nearly "
                  "everything — and 22 further metrics add no information on unseen clubs.",
             body="Across 160 Premier League squad-seasons, one variable outperformed the full metric "
                  "set out of sample, which argues for a simpler chance-creation KPI than most models "
                  "use. Comparing 168 transfers against same-position benchmarks, final-third "
                  "involvement held up across clubs better than xG+xAG output did.",
             fig=f"{BASE}/DSO 579 - Premier League Possession Analysis (2025 Spring)/Git Version/figures/what_predicts_chances.png",
             repo="https://github.com/Semin1c/pl-possession-and-box-entry", stack="Python · cross-validation · recruitment analytics"),
        dict(tag="La Liga · 380 matches", title="Where Home Advantage Comes From",
             stat="p = 0.54", label="crowd effect, once quality is controlled",
             desc="The home edge is territorial, not finishing. Crowd size stops predicting anything "
                  "once you account for who fills big stadiums.",
             body="Home sides create 1.484 expected goals to 1.121 while converting at an identical "
                  "rate — so the advantage is about where the ball goes, not what happens when it "
                  "arrives. Attendance looks like an explanation until club quality is held constant. "
                  "The referee spread sits inside what random shuffling produces.",
             fig=f"{BASE}/DSO 579 - First Goal Scoring Analysis (2025 Spring)/Git Version/figures/crowd_confound.png",
             repo="https://github.com/Semin1c/laliga-home-advantage", stack="Python · permutation testing · xG"),
        dict(tag="MLS · Europe's big five", title="Competitive Balance, Reversed",
             stat="0.315", label="points-per-match spread, lowest of six",
             desc="On parity, MLS beats every one of Europe's big five — on two independent measures, "
                  "across fourteen seasons.",
             body="The project started by assuming the opposite and coding it into the target variable. "
                  "Tested properly, MLS runs the tightest spread of the six leagues while Bayern took "
                  "11 of 14 Bundesliga titles. The classifier I first reported at 88–90% accuracy was "
                  "riding an 85.6% majority class; corrected, it reaches 0.954 AUC.",
             fig=f"{BASE}/DSO 579 - MLS vs European League Analysis (2025 Spring)/Git Version/figures/competitive_balance.png",
             repo="https://github.com/Semin1c/mls-vs-european-leagues", stack="Python · scikit-learn · SHAP",
             viz=dict(
                 title="How evenly matched is each league?",
                 sub="Spread of points per match within a season, averaged 2010–2023. Lower means closer.",
                 max=0.50,
                 rows=[("MLS", 0.315, "0.315", True),
                       ("Ligue 1", 0.415, "0.415", False),
                       ("Bundesliga", 0.449, "0.449", False),
                       ("La Liga", 0.464, "0.464", False),
                       ("Premier League", 0.473, "0.473", False),
                       ("Serie A", 0.476, "0.476", False)],
                 note="Points <em>per match</em>, because MLS and the Bundesliga play 34 games "
                      "while the rest play 38. Over the same period Bayern won 11 of 14 Bundesliga titles.")),
        dict(tag="NBA · 10 seasons", title="Schedule, Travel & Rest",
             stat="~61%", label="win rate with a 2+ day rest edge",
             desc="Separating travel, rest and opponent sequencing from team quality across 300 "
                  "team-seasons, to see what the calendar is worth before a ball is thrown.",
             body="Rest advantage, back-to-backs and schedule compression translate into differences "
                  "of up to roughly five wins across a regular season — enough to matter for planning "
                  "and for reading a standings table honestly.",
             fig=None,
             repo="https://github.com/Semin1c", stack="Python · schedule modelling"),
    ],
    skills=[
        ("Analytics & modelling", "Python · SQL · R · Regression · Classification · Clustering · Time series · Predictive modelling"),
        ("Sports data", "Team & player evaluation · Match analysis · Performance & tracking data · Schedule and travel analysis"),
        ("Tooling & BI", "Power BI · Tableau · R Shiny · Streamlit · APIs · ETL · Data validation · Git/GitHub"),
        ("Languages", "English and Chinese (bilingual) · Spanish (intermediate)"),
    ],
    contact_title="Open to sports analytics roles",
    contact_lede="Looking for analyst positions with clubs, leagues and performance groups, "
                 "starting May 2026. Email is the fastest way to reach me.",
),
}
