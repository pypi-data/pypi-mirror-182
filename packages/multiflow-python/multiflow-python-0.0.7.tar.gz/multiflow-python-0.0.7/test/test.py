import multiflow

import asyncio

async def main():
    w = multiflow.Workflow("wKSR3571FDZvCahW7XqM")
    x = await w.run_async("- In 2013, Snowden contacted journalist Barton Gellman and disclosed 9,000-10,000 documents exposing the PRISM electronic data mining program. Greenwald and Poitras published articles about the leaked documents in The Guardian and The Washington Post.", "Critics say that the NSA's spying programs are a violation of privacy and have called for more transparency and oversight. In 2016, US intelligence officials released a report that said Snowden's leaks had 'damaged US national security on a scale that few other intelligence leaks in US history have done.'")
    print(x["outputs"])

if __name__ == "__main__":
    asyncio.run(main())
