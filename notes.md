Software engineering is dead. Long live Software engineering! Surviving and thriving in this brave new agentic era

Software engineering has changed. Models and tooling have passed a threshold, it's simultaneously painful and exhilarating, our roles in the process are changing. There is a lot to deal with: the emotional responses of our own personal Kübler-Ross change processes, the huge amount of noise, options, marketing hype, the explosion of innovation and how on earth to keep up with the eye-watering pace of change! Incredible productivity gains are possible and increasingly expected in the boardroom, but resources are not infinite, we must consider the environmental impact. We're also expected to ensure quality while moving towards a world where we won't be able to review every line of code. We need to come to terms with the redefinition of the value that we add.

In this hopefully positive and optimistic talk, Andrew will share some practical advice on how to shift the mindset, what new things are important to understand, how to spot the things which will likely last and some pointers on how to get started, using real world apps and demos probably using Brady Gaster's Squad, Aspire and Aspire tests.

---------------------------------------------------------------------------------------------------------------------------

Ideas: could it be a retrospective on AI? with an animated SVG retro board?
- good, bad and ugly?

- Intro									graveyard, gravestone RIP, Ai robot filling in grave?
- what's happened?						race finish line, AI vested person/robot surging ahead
- what's good?							
- Demo?
- what's bad?							AI character in evil liar etc
- what's next? (end with actions)		long windy road ahead/ road to the machine city from the Matrix

## Intro

- RIP software engineering as we knew it
- wasn't determinism something we liked?
- the whole thing feels like a bad idea, unregulated capitalism is ill-equipped to handle the existential risks of AI
	- gold rush/arms race
- there is potential danger ahead though if we are not careful
- Quebec Bridge bridge disaster 29th August 1907, Iron rings and constant reminder,  Lévis

### Emotional responses / Resistance is futile!

- Ours is not the first, nor will it be the last industry to be changed forever by AI
- Kübler-Ross change processes
- what is the value we add?
	- we are the arbiters of change, not writers of code
	- it was never about the code, although thats how we identified ourselves
	- need to shift our value earlier in the process
	- plenty of things still needed from humans: 
		- ideas
		- sanity checking for ideas
		- domain knowledge
		- interpretation of the real world, domain modeling, event storming etc
		- learnings from failures
		- architecture & distributed systems strategies
		- systems thinking
		- discerning overcomplexity with respect to the complexity of the problem 
		- plain old common sense
		- oversight of test fitness, that tests adequately prove that the system is doing what it should, become hugely important
		- anything truly new or novel, this is pretty rare, but models can only remix existing things from their training corpus or things you point them at

### Pace of change

- Cutting through the crap
	- the huge amount of noise, options, marketing hype
	- github stars are useful
	- your own experimentation is massively important
	- 
	
	
- state of the art
	- Gas town, Beads & Dolt, OpenSpec, Speckit, BMAD etc

What should we be aiming for?
- Steve Yegges levels
- introduce the Risk spectrum, how far/fast we go, what we compromise on, what we care about, what we review all depends on what we are building, criticality and risk e.g. nuclear reactor control, medical tech, defense tech, even financial transactions require more rigour, scrutiny and deep understanding of the code/inner workings. A SentimentChecker app, who cares!

- Tools 
- Claude, Github Copilot CLI, Open Code
- MCP servers
- Skills
- Github Agentic workflows
- Squad (more later)

- Models
	- commercial frontier / open wieght
	- context windows and why they are important
	- who's on top at the moment?
	- pricing
	- interesting developments - Google tensor
	- how to compare?
	- how to choose?
	
- Control
	- dangerouslySkipPermissions (claude)
	- yolo (Copilot)
	- sandboxing
	- harness
	
- Concepts
	- use AI to build AI (turtles)
	- David Whitney Agent alongside etc

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

### Things which still need to improve

- working accross repos, especially with the shift towards unix philosophy
- enterprise level memory, storage and context efficient retrieval
- guard rails, everyone is trying to build their own, we should probably converge on some standards
- safe use of secrets

### Crystal ball

- what will the future look like?
- riskiness
- shapes and sizes, unix philosophy, ethemeral code?
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

### Dark side

- project lavenda
- we are literally throwing money and power at a very small number of US tech companies/MAGA
- massive environmental impact
- running local open weight models via ollama is a thing
- junior jobs
- lack of a professional body

- AI vampire, dopamine, slot machine, burnout, who should benefit from the productivity increase?

### Call to Action
- LETS NOT STOP HIRING JUNIORS!!!
- learn together, level eachother up
- remember the Risk spectrum








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

Folder	Added	Deleted	Total	%
.squad	+4,579	-6	4,585	41.8%
tests	+4,244	-10	4,254	38.8%
src	+1,253	-29	1,282	11.7%
docs	+843	-1	844	7.7%
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

