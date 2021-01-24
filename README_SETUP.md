This README was written by nicholas craycraft.

This repo is a clone of the https://github.com/bingo-todd/Gammatone-filters repo

I have modified the examples so that most of them actually run and so that the repo can be run in a docker container.
When the examples are run, they should produce the same output as in Gammatone-filters\examples\images
The images will write to Gammatone-filters\output

currently, all tests appear to produce the expected output except for the stimulus restore aligned tests which give incorrect output (reason TBD),
and the validate tests which fail to run due to us not having the detly/gammatone library installed.

To run the docker project and example code do the following:

1) cd to Gammatone-filters

2) docker build . -t gammatone

3) docker run --name=[CHOOSE A NAME] -it gammatone:latest bash
(this will open the docker bash and run the container)

4) ./runexamples.sh 
(run each python example)

5) open a separate cmd window and cd to Gammatone-filters

6) docker cp [USE THE SAME NAME]:/app/src/output ./output
(this will copy the output to your local machine which makes it easier to review the results)