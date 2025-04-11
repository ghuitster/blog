Title: Migrate CI Pipeline to AWS
Date: 2019-04-19
Category: Work Thoughts

The past two months at work have been crazy. Here's my story.

Our integration/branching strategy is to have engineers branch straight off of master for each work item they want to complete. When the engineer is ready to integrate their work they open a pull request from their branch to master. We then kick off lots of tests to prove their code is good. If all the tests pass, we merge their code into master. That testing process executes on hardware in our building. We (mostly me) made the mistake of adding all this testing without understanding capacity, growth of the company, and wanting to do EVEN MOAR tests. The result: our testing was slow, unreliable, had low throughput, and frustrating. Classic bottleneck we should optimize.

Enter AWS. An "unlimited" place to allocate computers. A great battle buddy of mine, Craig, paired up with me to proof of concept we could do this in AWS. After hours of troublesome issues, learning the limitations of the "T" series of machines, chasing our tails on specific tests, we got the POC to work! We presented our findings and preliminary cost estimates to the powers that be. And the feature got planned! Wahoo!

Then the AWS team at work began to make it happen. Around 15 awesome people worked to help improve the lives of their fellow engineers. Pretty much all of us had no idea how to do AWS anything, or how to set up networking, but everyone dove in like champs. About a month later, many late nights, me getting sick twice, and lots of intelligent people making many intelligent decisions, we were able to turn it on! Our capacity for handling pull requests increased by something like 1000%. Duration of the testing went down by 73.8%. Our reliability increased by about 35%. And the best part? It's about 20% as expensive as the pessimistic projections we were given :)

A long couple months. And a really exciting couple months.