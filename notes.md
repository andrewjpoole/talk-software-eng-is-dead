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

## ToDo




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

### Dark side

Nvidia ??
Neural scaling laws

- git work trees

## After slides done...

- update retro board
- add consistent accents
- make title placement consistent
- benefits of squad page?

Some kind of project attribution, per session for token usage?

Amazon tells engineers to review all ai output


at what point does an agent cost the same or more than an engineer?

fast : cheap : good