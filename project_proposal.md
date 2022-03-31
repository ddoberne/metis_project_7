# The Filthiest
## Background
Twitter user Rob Friedman aka "PitchingNinja" has made a career for himself on social media posting short clips of pitchers in baseball throwing at their best.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Devin Williams, Absurd Airbender. 🛸 <a href="https://t.co/ZMFgk0owHc">pic.twitter.com/ZMFgk0owHc</a></p>&mdash; Rob Friedman (@PitchingNinja) <a href="https://twitter.com/PitchingNinja/status/1508567376438173699?ref_src=twsrc%5Etfw">March 28, 2022</a></blockquote> 

Having spent many hours scrolling through his Twitter feed, I can attest to the entertainment value of a highlight real of great pitching. The goal of this project will be read in baseballsavant data on a daily basis and report back the filthiest pitch(es) thrown in a major league game on the previous day that ended in a positive outcome for the pitcher. Each pitch is logged on baseballsavant, along with the outcome, velocity, rotations per minute, vertical break, and horizontal break. I will read in all the pitches thrown the previous day, then return the pitch(es) that had the highest velocity, most vertical/horizontal break, and most RPMs that ended in a strike, foul, or out.

If successful, this audomation will select specific pitches to highlight for a highlight reel, and reduce the need to sift through lots of video to find content.

## Data
Data will be updated on a daily basis and be acquired through web scraping. The end result will be presented as a web application. It will include a visualization of the ball's flight path as it travels from the pitcher's hand to its target.
