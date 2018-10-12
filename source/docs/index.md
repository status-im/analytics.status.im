---
id: index
title: Better Data For Everyone
---

# Status is an ambitious project.

As we’ve grown to a team of 100+ individuals scattered across the world, it’s become increasingly important to align people around near-term goals that keep us moving toward our greater vision of a decentralized web. 

So, some backstory first:

---

We implemented Mixpanel tracking earlier this year on an opt-in basis only. We presented users with the choice to share data during onboarding, and we later made changes to this screen to remove dark patterns that may have subtly influenced people to opt in. 

We tracked only high-level, anonymous data, and we were [transparent about what we tracked](https://wiki.status.im/Help_Improve_Status). We could observe patterns in how many users opened a DApp, sent a message or made a transaction. But we knew nothing about which DApps were opened, which chats were most trafficked, or how much was being transacted. 

Collecting this data helped us understand how big an impact Mainnet had on transactions, how relatively popular DApps are with our users, and how far we still have to go to make every day use of Status a reality. 

---

We did all this with good intentions. We wanted data to help us make our app more usable and further our ultimate goal, mass adoption of Ethereum.

**The trouble is, mass adoption of Ethereum means nothing if you’re sacrificing on the core values of the Ethereum community to get there.**

In focusing so much on the portion of our mission we could measure, we overlooked some of the ideals that brought us here in the first place. Our failure to adhere came to a head during a [recent workshop](https://www.youtube.com/results?search_query=Status+July+2018+Security+Meetup) in Basel, Switzerland. After a day spent discussing Status’ [organizational principles](https://discuss.status.im/t/principles-from-basel/175) and our [wall of shame](https://hackmd.io/fpqnTU4pRTKVqcUijrZwxg?view), it was too glaring to ignore—or rather, forgive—that we’d strayed off-course. 

We are committed to **security**, **privacy** and **decentralization** and we can not compromise on these elements out of anything other than complete necessity. 

Regardless of our intentions behind using Mixpanel, a trusted intermediary, it was not a necessity. We’d put our principles at risk by sending user data to a centralized third party. 

An HTTP request is all it takes to expose a host of user data to an information broker. 

Mixpanel is not immune from being hacked—not long ago, the service itself accidentally leaked the value of user passwords in its dashboard events. 

And even if users explicitly grant consent for tracking, they probably don’t know how their data is being collected and stored.

---

Our founding members created Status because of their strongly-held beliefs around privacy, security, and personal liberty. This has attracted contributors who share in those beliefs, but who are also excited by the opportunity to build a cool product while performing a specific role.

It’s easy for us to default to what we know. As a product manager, I was the first to celebrate product analytics as a form of accountability.

We’re not entirely finished with data, either. A custom dashboard using publicly available, on-chain data is [in the works](https://github.com/status-im/ideas/tree/18c7a4bfc3109e097a89573ddb52dd147f21cabb/ideas/266-methrics) so that we can remain responsibly informed about usage *and* actively work to prevent metadata leakage in our products.

In order for us to build the product that best serves our community, we’re asking for your input and active participation. You’re always invited to collaborate with us on our [forum](https://discuss.status.im/), across social channels, directly in our [codebase](https://docs.status.im/docs/contributor_guide.html) and, of course, within [Status](https://get.status.im/chat/public/status).