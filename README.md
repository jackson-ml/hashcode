# Hashcode 2020

#### Collaborated with Kaito Nakatani, Jason Ngo, and Jiajie Ma at Haverford College.

This repo contains our solution to Google's 2020 Hashcode programming competition, where we work together as a team of four to solve an optimization problem in 4 hours. I organized a team with a few other math/cs dual majors that I had classes with to take on the challenge. We performed well during the event, reaching 41st in the US and 771st globally.


### The Problem

The Hashcode 2020 problem was centered around Google Books. Google Books is a vast digital archive of information, but the logistical problem of how to actually enter books into that archive raises interesting questions. Should short books be prioritized? Or ones in high demand? To solve the Hashcode 2020 problem, we had to optimize the total "book score" that our algorithm scanned, given constraints about the rate that libraries can scan books, the time it takes to enroll a library in the program, the time that our algorithm runs, and individual book values.

### The Rules

We were given 4 hours from the release of the problem to the deadline to submit our best algorithm results. Only one library can undergo the signup process at a time, but after a library is signed up, it scans books at a fixed rate of books per day. Our input consisted of text files with lists of numbers representing the constraints of each dataset: how many days we had to operate, how many libraries there were, how many days it took them sign up, how many books per day they could scan, what books they had, and how valuable those books were. The final score is just the total cumulative score of every book that is scanned. This is the basic idea: (image credit to Google)

![Problem structure](https://miro.medium.com/max/875/0*Ki2R5KQ6TfrjUGF2)

### Our Process

We decided pretty quickly on a greedy approach, to always try and sign up the next best library. It seemed like the most natural way to solve the problem, as we had lots of information to determine what the value of any given library was. From there, the only real hurdle to developing the algorithm was figuring out how exactly we were defining the value of a library. As I mentioned earlier, our team was made up of math/computer science dual majors; some of us leaned more heavily in the math direction and took my algorithm advisory roles, while others did more of the coding. The commits on this repository accurately represent the code created by the respective contributors.

I quickly realized that we would need a good data structure for representing libraries, so I started writing up our data parsing method while we were still discussing the algorithm, making sure that everyone understood and was happy with the decisions I made. After we decided on the algorithm, we divided into two pairs: one to work on the algorithm, and one to work on the "post processing" of the data produced by our algorithm about what order to signup libraries and scan books into the output format requested by the problem. The algorithm to decide on library order was my idea, so I wrote that and Jason Ngo did book order (within each library); we collaborated on the postprocessing.

### The Algorithm

A greedy algorithm is all about signing up the next best library and scanning the next best book, so the key to the algorithm was evaluating what the "best" algorithm was. Clearly, the more valuable books were in the library, the more valuable the library was. The tricky part was to simultaneously account for the timing; how many books per day the library can scan, and how long it takes the library to sign up. As a further gotcha, a book can be within multiple libraries at once, and you don't score extra for scanning the same book again. Thankfully, working with a greedy algorithm allows us to retain a notion of "how many days we have remaining" and "already scanned books." Using these, I came up with a "library score" that was essentially based on the idea of "unique book score." Unique book score  means that we evaluate the number of unique books that the library can scan if we started signing it up immediately, then took the sum of the score of that many unique books (in order of value, of course). While this captures the value of a library reasonably effectively, it doesn't accurately include the time cost of signing up the library, which is important for order. Because we can only signup one library at a time, it's important to signup libraries with shorter signup times first, so that we can have more libraries scanning books earlier. If we think about unique book score as the value of the library, and signup time as the cost, it makes sense to score a library overall as value over cost; in this case, unique book score over signup time. That's exactly what I proposed to the group, and nobody else had any particular better ideas. One of the mathy people applied it to the simple example dataset given (a_example.txt) to make sure that it produced the optimal result, and then we quickly started coding as we had a pretty strict time constraint and wanted to retain time to fine tune or adapt the algorithm if it didn't work.

### The Code
parse_data.py contains the code I wrote for parsing the input text files into a list of library objects and book scores. It's relatively straightforward. score_libraries.py contains the starter function `get_library_order` which calls the parsing function and outputs the order which the libraries should be scanned according to the algorithm. book_order.py contains the function `get_book_order` which determines the order which each library should scan its books. Finally, postprocessing.py turns this into the output required format by the problem. 


### The Challenges

There was one chief challenge for our algorithm: runtime. One of the datasets was particularly massive, and our algorithm didn't finish after a few minutes. This posed a problem as we weren't certain whether it would ever finish, and failing to post a score for one of the datasets could lose a massive amount of points. We solved this by first trying to eliminate any unecessary loops and replacing them with list comprehensions and other relatively fast Python programming patterns, but it was still slow. The, we added loading text to our algorithm. While debugging, we had it print it's % completion every so often. This allowed us to time the algorithm and figure out that it actually would solve the dataset in an hour. This gave us security in the fact that we'd have an answer to post when the time came, and an hour to think of anything better for this particular dataset. Our result for this dataset ending up actually being pretty good, so we didn't have to rerun the algorithm.

Further, I realized with only 45 minutes to go that there was a slight flaw in the unique book score algorithm; it didn't properly account for the idea that some libraries might get more value out of being early than others, for example. If a library only has one incredibly valuable book but plenty of other low value books, it doesn't necessarily need to go early; it could be signed up at the last minute, but our algorithm might want to sign it up early because the library has high value as a whole. Unfortunately, our algorithm doesn't attempt to measure the actual score cost to scheduling libraries earlier or later, only the value of libraries at the present moment. I tried a couple ways to account for this, but nothing gave better results than our previous algorithm. In the process of modifying the algorithm however, I realized that arbitrarily weighting certain parts of the unique book score could possibly result in a better score, as unique book score is not an absolute measure of optimality but an approximation of how much worth a library can produce in the remaining interval given a certain signup time. This improved our scores on some of the datasets by a few thousand points, so while I didn't solve the problem, I did find some useful information I was able to incorporate into our solution.


### The Results

Our team `math is better than cs` scored **26,561,032 points, taking 41st in US of around 500 and 771st globally of around 10,000**. The top score was 27,203,691, so we got fairly close; around 97.6% of the best result. I suspect that the results above us found some way of accounting for the property I mentioned above, the way the timing of a library actually affects its library. We were able to rise around 60k points and 100 global placements due to the last minute optimizations (by arbitrarily weighting certain parts of the unique books score computation) I mentioned above. All in all, I'm pretty happy with our performance, given that only two of us really coded all that often and it was all of our first experiences with coding competitions. I look forward to next year!




