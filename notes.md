Software engineering is dead. Long live Software engineering! Surviving and thriving in this brave new agentic era

Software engineering has changed. Models and tooling have passed a threshold, it's simultaneously painful and exhilarating, our roles in the process are changing. There is a lot to deal with: the emotional responses of our own personal Kübler-Ross change processes, the huge amount of noise, options, marketing hype, the explosion of innovation and how on earth to keep up with the eye-watering pace of change! Incredible productivity gains are possible and increasingly expected in the boardroom, but resources are not infinite, we must consider the environmental impact. We're also expected to ensure quality while moving towards a world where we won't be able to review every line of code. We need to come to terms with the redefinition of the value that we add.

In this hopefully positive and optimistic talk, Andrew will share some practical advice on how to shift the mindset, what new things are important to understand, how to spot the things which will likely last and some pointers on how to get started, using real world apps and demos probably using Brady Gaster's Squad, Aspire and Aspire tests.

promised themes from the abstract:
- emotional responses
- signal:noise ratio and pace of change, innovation, keeping up
- redefinition of the value we add
- productivity gains (hype vs reality)
- practical advice
	- whats important to understand
	- spotting things which are likely to last, crystal ball
	- pointers on how to get started, squad
- ensuring quality
- darker sides
- demos- now case studies

---------------------------------------------------------------------------------------------------------------------------

current structure:
- RIP SE
- whats happened? timeline
- emotional responses
	- change curve
	- where I am personally
- hype cycle
- pace of change
- effects on health
- humans are still nessecary
- what things are important [models, tools, concepts]
- how to get started? [squad]
- What should we be aiming for? [productivity gains, yegge's levels, risk spectrum]
- Risks [capitalism and industry failures, quebec bridge]
- case studies
- improvements needed
- cystal ball
- dark side
- retro board

## Intro

- RIP software engineering as we knew it
- wasn't determinism something we liked?
- the whole thing feels like a bad idea:
	- sometimes industries do something even when they know its the wrong thing to do
		- e.g. Tobacco (cancer), Fossil Fuel (climate change), Phamaceutical (opioid pankillers/addition), Forever chemicals (3M & DuPont toxic non-stick and water repellant coatings), Automotive industry (fuel tank fires, faulty ignition switches. diesel emmissions), Social Media (mental heath/addiction), Food & Beverage (sugar/obesity)
	- AI adoption  can be likened to a gold rush/arms race scenario where a kind of commercial fear of falling behind drives escalation/accumulation
	- unregulated capitalism is ill-equipped to protect scociety against these risks
	- AI could be seen as one such risk, for several different reasons

## Quebec bridge

- there is potential danger ahead though if we are not careful
- Quebec Bridge bridge disaster 29th August 1907, Iron rings and constant reminder,  Lévis
St Lawrence river was 3.2km (2m) wide at its narrowest
Main trade channel for Quebec, closed by ice during the winter, fast flowing, 5m tidal range, 58m deep at the middle
Commercial competition with Montreal, who already had rail connection to Toronto and other bridges planned
Dodgy tendering decisions
Span length changed without recalculating stresses May 1900
Assistant deposed for opposition to the calculations July 1903
Construction of main superstructure starts July 1905
noticable midpoint deflections observed, June 1907
predrilled rivet holes did were not lining up, disputes about whether the chords were bent during manufacture
manufacturer confirmed they were all straight when they left the yard
one chord A9L was dropped and bent and repaired (this was actually found to be the starting point of the collapse)
Some workers were worried enough to stay at home, there were also strikes due to working conditions
Chord AR9 was put under observation and its deflection increased from 19mm to 57mm!
work halted, while onsite-inspector went to see the principal engineer, but the foreman changed his mind Aug 27th
telegram sent to the local office but not the site "add no more load" Aug 29th
message was ignored until 5:15 when in a meeting they decided to defer the decision untill the next morning, at 5:30 the bridge collapsed

- lack of a professional body

### Emotional responses / Resistance is futile!

- Ours is not the first, nor will it be the last industry to be changed forever by AI
- Kübler-Ross change processes
	- Shock
	- Denial (disbelief, looking for evidence that it isn't true)
	- Frustration (recognition that things are different, sometimes anger)
	- Depression (low mood, lacking in energy)
	- Experiment (initial engagement with a new solution)
	- Decision (Learning how to work in the new situation)
	- Integration (changes integrated, a renewed individual)
	- Hopefully the we end up at the same hieght or higher than the starting point.
	- For a resctructure etc the initial stages can be quite rapid, for AI its been a long time coming
- what is the value we add?
	- it was never about the code, although thats how we sometimes identified ourselves
	- need to shift our value earlier in the process
	- plenty of things still needed from humans

### Pace of change

- Cutting through the crap
	- suprise + spread of information + impatient economic actors = frenzy 
	- the huge amount of noise, options, marketing hype
	- github stars are useful
	- your own experimentation is important	
	- share knowledge and level eachother up
	- dont try and read everything
		- I follow David Fowler, David Whitney, Brady Gaster, Steve Yegge, the odd news post that catches my eye.
	
- state of the art?
	- Gas town, Beads & Dolt, OpenSpec, Speckit, BMAD etc

### What things are important

- Models
- Tools 
- Claude, Github Copilot CLI, Open Code

#### Concepts

- Ue AI to build AI
- Add deterministic tools to the non-deterministic models
	- use tokens efficiently

- context and tokens
- git work trees

- MCP
	- standardised protocol for programs to expose capabilities to AI apps
	- defined in JSON
	- Tools
		- Functions that the model can call at will, could be anything, typed inputs and outputs, the human must approve
	- Resourses
		- Passive data sources, read only, controlled by the application
	- Prompts
		- Prebuilt instruction templates instructing the model to use the Tools and resources

	- Excellent examples Azure MCP, Aspire MCP

	- Cons
		- Security flaws, lacls built-in auth/granular permissions
		- Context window bloat, all tools are added to trhe context
		- Performance, can be slower than direct API calls

- Skills
	- whereas MCP is a relatively hard abstration, Skills are much softer
	- reusable, portable and modular package of instructions, scripts and resources
	- expressed in markdown SKILL.md
	- extend the functionality of an agent
	- anything you might need to do more than once or share with someone else, could be a skill
	
	- Cons
		- hard to test, use evals

- Github Agentic workflows

- Agent Harness [Agent = model + harness, Harness = orchestration loop + tool execution and sandboxing + context management + state & memory persistence + guard rails & safety]
	- sub agents
	- personas

- Squad

- Token efficiency tools
	- Serena 
	- codebase-memory-mcp https://github.com/DeusData/codebase-memory-mcp
	- Caveman

- Models
	- open weight = snapshot of trained model, download and run. Open source = includes training data, code, architecture etc 
	- context windows and why they are important
	- who's on top at the moment?
	- pricing
	- interesting developments - Google tensor, 10 years of development
		- Google have developed their own hardware Tensor Processing units (TPUs)
		- ASIC (Application specific integrated circuits) specific to AI, better than CPUs or GPUs
		- specific chips for training and inference
		- new design at every level, hardware, infra, network, cooling
		- Sparse cores especially for sparse data which normally slow standard processors
		- liquid cooling
		- Models built especially for the hardware
		- 30-80x higher performance per watt than traditional hardware

- Tools
	- Serena [efficient semantic code retrieval/editing/refactoring/debugging]
	- codebase-memory-mcp [tree-sitter, creates map of code, indexed 28M LOC linux kernel codebase in 3 mins] 120x fewer tokens 
	- RTK [CLI proxy, filters and compresses command outputs before reaching LLM] 60-90% token reduction
	- caveman ["why use many token when few do trick"] up to 75% redunction in output tokens

- Control
	- dangerouslySkipPermissions (claude)
	- yolo (Copilot)
	- sandboxing
	- harness
	
- Concepts
	- use AI to build AI (turtles)
	- David Whitney Co-design with Agents

What should we be aiming for?
- Steve Yegges levels
- introduce the Risk spectrum, how far/fast we go, what we compromise on, what we care about, what we review all depends on what we are building, criticality and risk e.g. nuclear reactor control, medical tech, defense tech, even financial transactions require more rigour, scrutiny and deep understanding of the code/inner workings. A SentimentChecker app, who cares!

### Real life case studies: Squad

- Resilience report tool
	- initial plan, curate a series of prompts to be used in ChatGPT/Perplexity
	- better to be split into deterministic and non-deterministic phases
		- scripts for the deterministic parts, written once by an agent and tested, same output each time called
		- skills for the non-deterministic parts which require natural language processing/sentiment analysis etc
	1. extract JSON data file from single Word document response - D - skill with script
	2. augment JSON data with summary/analysis of free text answers - ND - skill with prompt
	3. once all respones gathered, create new summary JSON file with summary/analysis/recommendations of all submissions for the setting - ND - skill with prompt
	4. read summary and response JSON files, check if summary is correct
	5. human sanity check summary and response JSON files
	6. load markdown template and create report - D - skill with script
	7. generate and insert graphics - D - skill with script
	8. send report
	9. once summary JSON files are available for all settings, use steps similar to 3-7 to create overall report

	If a survey tool with an API were to be used to gather initial responses, then a corresponding MCP server would be ideal to extract data from the API
	Or perhaps if we wanted to store the data in a database
	Or if the system were to scale up, we could have agents build an app for the whole thing

### Real life case studies: Squad

- Audited SQL query tool (trivial)
	- project outline 
	- introducing the squad
	- Github Copilot CLI
	- decisions
	- charter & history
	- suprisingly human commands 
	- github integration?
	- teams integration?

- real life case study CAMT mapping refactor (critical)
	- 700 line single mapper, covering all payment types, in & out, heavy use of undocumented Regex patterns, organically developed, everyone scared to go there
	- overdue a refactor, opportunity to aggressively refactor!
	- confidence tests
	- process(iterative, manual reviews and commits)
	- results
	
- comparisons/conclusions?

- pros and cons of Squad
	- beyond single repo squad?
	- squad on k8s
	- pluggable storage, so you can use Beads etc

### Productivity Gains

	- most people are seeing that generating code is much faster
	- people talk about 2 - 10x gains
	- but the writing of code probably wasn't the bottleneck
	- objectively I feel like our team is perhaps 1.5 - 1.8 x faster
	- difficult to measure
	- cost of tokens also increasingly important

### Things which still need to improve

- working accross repos, especially with the shift towards unix philosophy
- enterprise level memory, storage and context efficient retrieval
- guard rails, everyone is trying to build their own, we should probably converge on some standards
- safe use of secrets

### Crystal ball

- shapes and sizes, unix philosophy, ethemeral code?
- effect on teams?
- predicting which things will work & survive (mostly stuff we already know and use)
	- TDD
	- SOLID
	- agile practices / XP
	- established technologies
		- git
		- markdown
		- anything which will have been in the training corpus
- need to adapt our processes
	- keeping up with code reviews
	- keeping data secure
	- baking in security
	- token efficiency
- projects and product teams will have both a human and token resource budgets
	- all tokens will need to be attributed for cost accounting
- local models will become crucial to control costs




### Dark side

- Mental and physical effects
- AI vampire, dopamine, slot machine, burnout, who should benefit from the productivity increase?

Nvidia ??
Neural scaling laws
Mistral (French)


## Case studies

Case study 1 - ReportMapper change

This was a significant and critical change, required so that we can change the way we uniquely identify outbound payments.

Background

we have a correspondent bank, who has an API
we send automated payments (debits) through one endpoint
we synchronise transactions on our main accounts by calling another endpoint
the responses are CAMT intra-day and end-of-day files containing all transaction data (debits and credits)
the transaction data must be interpretted or mapped, the thing doing this is the ReportMapper
there is a lot of strange and complex logic in this area
A single static class with 700 lines of uncomprehensible regex, shared between all scenarios (all payment types, credit and debit)
Aim

```xml
<Ntry>
    <NtryRef>20260503-001</NtryRef>
    <Amt Ccy="EUR">1500.00</Amt>
    <CdtDbtInd>CRDT</CdtDbtInd>
    <Sts>BOOK</Sts>
    <BkTxCd>
        <Domn>
            <Cd>PMNT</Cd>
            <Fmly>
                <Cd>NTFR</Cd>
                <SubFmlyCd>MCOP</SubFmlyCd>
            </Fmly>
        </Domn>
    </BkTxCd>
    <ValDt>
        <Dt>2026-05-03</Dt>
    </ValDt>
    <AcctSvcrRef>REF123456789</AcctSvcrRef>
    <NtryDtls>
        <TxDtls>
            <Refs>
                <EndToEndId>E2E-987654321</EndToEndId>
            </Refs>
            <AmtDtls>
                <TxAmt>
                    <Amt Ccy="EUR">1500.00</Amt>
                </TxAmt>
            </AmtDtls>
            <AddtlNtryInf>INV-2026-0503; Customer ID: 998877; Project Alpha payment.</AddtlNtryInf>
        </TxDtls>
    </NtryDtls>
</Ntry>
```

we identified a better way to send a unique identifier along with automated payments, but required a ReportMapper change to read these identifiers on the way back in
Desired outcomes

safe way to make the nessecary change, without impacting all payments in and outbound
take the opportunity to vastly improve the ReportMapper
confidence that it would work
ability to quickly switch back if something didn't work
Approach

100% AI planned, tested, implemented and documented
100% human reviewed
Devised a set of 'confidence tests' which run the new ReportMapper against an amount of live CAMT files and check the results against an export of live transaction data from the same period.
these were written by the Tester agent, Lisa, but isolated from the actual test data and strictly only run by merged
new ReportMapper run against 10,000 live historic transactions
actually lead to discovery of two 'interesting' behaviours of our correspondent bank's systems
work split between Squad members
excellent test coverage and documentation
probably the most pre-tested code change I've ever been responsible for
Actual Outcome

We created a multi-step mini-cutover plan with checkpoints and rollback, just in case
But in the end it worked perfectly!
Typically something went wrong immediately after, but after 20 stressful minutes, realised it was not related
We now have a strategy per payment type and direction
We are also seeing RemittanceAccount info correctly parsed on transactions where the old legacy ReportMapper was not able.
Analysis of PR #365 — Task/253602 reference changes phase 1 (merged, 70 files, 10,968 LOC):

|Folder|Added|Deleted|Total|%|
|---|---|---|---|---|
|.squad| +4,579| -6	 |4,585	|41.8%|
|tests | +4,244| -10 |4,254	|38.8%|
|src   | +1,253| -29 |1,282	|11.7%|
|docs  | +843  | -1	 |844	|7.7% |


Observations

Speed, this change was large, it was complex and performs a critical job, everyone was afraid to go there. Speed is difficult to measure, but:
the ideation process was much faster and pretty high quality (the more options considered, the higher the chance of selecting the correct one)
the writing of code and tests was much faster than writing manually, I was able to focus on the design and guidance and also doing this alongside other work
I would estimate it would have taken at least three times as long to do manually.
The PR looked big, but no legacy code was removed yet - there will be a significant cleanup task to follow
The .squad folder is interesting, its large, but it represents the squad members 'learning' the domain and from steering from human users. Plus it could potentially be compacted if needed.
Slides

animated diagram for the background?
screenshot of confidence test results?
piechart of PR split?
Case study 2 - Audited SQL query tool

PoC no risk while building, minimal risk after adoption

Background

occasionally need to do database updates
we have a pipeline based script runner tool to safely execute scripts which have been PR'd and merged
but writing and testing the scripts is still tricky
Aims

we need a tool to make investigation of data issues and the writing and testing of update scripts easier
the tool must be strictly read only
we need to audit the read queries that engineers are performing
some mode/strategy to aid writing and testing of update scripts
also with the safe help of an LLM with the context of the source code if possible
Desired Outcomes

A tool to demo
Approach

100% AI generated
I am only interested key parts of the C# code, to garuntee the readonly-ness
I have never looked at the frontend code, may even scrap and regen in a different form etc
Actual Outcome

working demo able to run queries in the monaco editor in an hour or so
schema explorer and code completion in a couple more hours
query audit trail posting to github and AzDO in another hour
added local LLM integration via ollama in a few more hours
Case study 3 - UI mockup in high level project workshop with stakeholders

Background

workshop to reach alignment on next phase of major project
discovery of actual process, and unfitness of current tooling
difficulties visualising UX options
Aims

an easy way to try out UX ideas
Approach

create a detailed initial prompt describing the problem/tasks and an initial UX idea
reference the provious UI mockup for consistency
have the agent create a single html file with styling and javascript, with canned data, which can be downloaded and run by anyone using a browser
when an idea emerges, simply prompt the agent to try it
keep what works, revert whatever doesn't
have the agent document the changes in a markdown document with diagrams and key decisions/dicoveries etc
Actual outcome

enjoyment and collaborative sense of progress
clarity on the direction in terms of UX

## ToDo

- improve RIP drawing or replace with ai generated images
- some need images/quotes removing/adding
	- crystal ball x 2
	- improvements
	- pace of change x 2
	- productivity gains
	- risks
- Concepts slide(s)
	- tokens, credits, cost	
	- Control (YOLO, dangerouslySkipPermissions, sandboxing)
	- running local models (ollama)
	- use AI to build AI
- Pricing
	- token prices actually dropping over time
	- demand rising, GPUs, RAM, compute costs rising
	- subsidised subscription models easy for enterprise to budget for
	- Anthropic appear to be the only company charge true cost rates
	- once enterprises are sufficiently hooked, raise the subscription prices
	- API per token pricing likely to be much higher -> token efficiency tooling and local models becoming more important
	- cartell/drug dealer/gateway drug

- Ensuring Quality

- Case studies slides improvements

- sketch ideas

A set of 11 hand-drawn sketch panels arranged in a neat grid on white background. All panels are black and white with gray shading, drawn in pen-and-ink style using 3px thin black strokes for outlines and broader soft gray hatching strokes for shading, simulating hand-drawn illustrations. The sketches should be moderately complex but made of lines rather than large complex shapes so I can animate them using css by stroking the paths so they look like they are being hand drawn. Two recurring characters appear throughout: a human figure (young, casual clothes, expressive face) and a humanoid robot with the letters "AI" printed on its chest. The 7 panels are:
Panel 1: Human standing in a robot shop looking completely overwhelmed, surrounded by robots of wildly different shapes and sizes — some humanoid, some boxy, some on wheels — displayed on shelves and standing on the floor, human has wide eyes and raised hands in confusion. There are posters and advertising and marketting materials everywhere, overwhelming the human.
Panel 2: Human and the humanoid AI robot arm wrestling at a table, both straining, human looking determined but struggling, robot calm and steady.
Panel 3: Human slumped over asleep in a chair, mouth open, zzz bubbles, while the humanoid AI robot stands nearby buzzing with energy, building something, clearly full of activity.
Panel 4: Human dozing off in a supervisor's chair, hard hat slipping off head, while 5 humanoid AI robots energetically work on a construction site — carrying beams, hammering, using tools — all full of energy.
Panel 5: Human standing with arms folded and a smug or exasperated expression, looking down at the humanoid AI robot which has toppled and collapsed into a crumpled heap on the floor.
Panel 6: Human and humanoid AI robot skipping together side by side, holding hands, both with happy expressions, motion lines suggesting joyful movement.
Panel 7: Human is running very fast because the humanoid AI robot is pushing the human along, both are enjoying going so fast. 
Panel 8: Human in a workshop bending over the humanoid AI robot laid on a table, tools scattered around, human wearing magnifying goggles, poking and experimenting on the robot's open chest panel.
Panel 9: Human looking worried a little scared of the humanoid AI robot who is looking menacing and evil.
Panel 10: Humanoid AI robot is holding a shovel dropping dirt from a pile to fill in a deep open grave where some books and computer equipment including a keyboard can be seen at the bottom of the grave, at the head of the grave is a gravestone saying "R.I.P Beloved Human Written Code" and the dates "1940s - 2025" the human is not in this sketch at all.
Panel 11: Human supervises while the humanoid AI robot installs a jetpack on to the back of a second humanoid AI robot.
Grid is clean and evenly spaced, each panel has a thin border, consistent character proportions and sketch style throughout, whimsical editorial cartoon aesthetic.

perhaps just 
1, 3, 6,  7, 8 and 10

Panel 1: Human standing in a robot shop looking completely overwhelmed, surrounded by robots of wildly different shapes and sizes — some humanoid, some boxy, some on wheels — displayed on shelves and standing on the floor, human has wide eyes and raised hands in confusion. There are posters and advertising and marketting materials everywhere, overwhelming the human.
Panel 3: Human slumped over asleep in a chair, mouth open, zzz bubbles, while the humanoid AI robot stands nearby buzzing with energy, building something, clearly full of activity.
Panel 5: Human standing with arms folded and a smug or exasperated expression, looking down at the humanoid AI robot which has toppled and collapsed into a crumpled heap on the floor.
Panel 6: Human and humanoid AI robot skipping together side by side, holding hands, both with happy expressions, motion lines suggesting joyful movement.
Panel 7: Human is running very fast because the humanoid AI robot is pushing the human along, both are enjoying going so fast. 
Panel 8: Human in a workshop bending over the humanoid AI robot laid on a table, tools scattered around, human wearing magnifying goggles, poking and experimenting on the robot's open chest panel.
Panel 10: Humanoid AI robot is holding a shovel dropping dirt from a pile to fill in a deep open grave where some books and computer equipment including a keyboard can be seen at the bottom of the grave, at the head of the grave is a gravestone saying "R.I.P Beloved Human Written Code" and the dates "1940s - 2025" the human is not in this sketch at all.

## After slides done...

- Notes
- Ordering of slides/sections
- practice timings

Some kind of project attribution, per session for token usage?

Amazon tells engineers to review all ai output



Could an economic calulation be contrived?
1 sprint == 25 story points in 2 weeks (10 working days) == £20k
1 PO, 5 engineers == 6 people, £20k/6 = £3,333 per person
10 days * 5 engineers == 50 engineer days
£3,333 / 10 == £330 per day
opus tokens for £330?
would velocity rise due to agents?
at what point does an agent cost the same or more than an engineer?

promised productivity gains : quality/reviews/understanding/certainty : controlled costs/cost savings - can only have 2! Venn diagram