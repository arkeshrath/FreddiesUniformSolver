# Freddie's Missing Uniform

Freddie's mischievous friends have stolen his Mailchimp uniform (again) and have left him a secret message indicating
where they've left the items. Since Freddie can't go to work without his uniform, he's desperately asked for your help
to find his things.

His friends have left him large sheets of transparent grid paper, similar to the ones used with
[overhead projectors](https://en.wikipedia.org/wiki/Overhead_projector) and some instructions to go along with them.

The page with the shortest amount of instructions contain the following lines:

```
cell at x=0,y=0
cell at x=11,y=10
cell at x=3,y=0
cell at x=14,y=9
cell at x=14,y=1
cell at x=11,y=9
cell at x=11,y=1
cell at x=14,y=8
cell at x=13,y=8
cell at x=1,y=2
cell at x=12,y=8
cell at x=11,y=2
cell at x=14,y=7
cell at x=11,y=7
cell at x=14,y=6
cell at x=0,y=6
cell at x=0,y=4
cell at x=11,y=4
cell at x=3,y=6
cell at x=8,y=10
cell at x=8,y=0
cell at x=6,y=0
cell at x=8,y=1
cell at x=6,y=9
cell at x=6,y=1
cell at x=8,y=8
cell at x=6,y=8
cell at x=6,y=2
cell at x=6,y=7
cell at x=6,y=6
cell at x=6,y=4

fold up along y=5
fold left along x=7
```

Freddie theorized that the first section of the instructions correspond to coordinates on the grid paper and has marked
them in black (⬛). He's already gotten a head start and has used the coordinates `x=0` and `y=0` to represent the
top-left most cell with the value for `x` increasing to the right and the value for `y` increasing downward. For
example, notice that the cell in `x=6` and `y=2` has been filled in by Freddie:

```
⬛⬜⬜⬛⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬜⬛⬜⬜⬛⬜⬜⬛
⬜⬛⬜⬜⬜⬜⬛⬜⬜⬜⬜⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛
⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬛⬜⬜⬛
⬜⬜⬜⬜⬜⬜⬛⬜⬛⬜⬜⬜⬛⬛⬛
⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬛⬜⬜⬛
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬜⬜⬜
```

Below the coordinates, Freddie points out, is a list of instructions on how to perhaps fold the transparent grid paper.
So for the first instruction, `fold up along y=5`, would indicate the following line:

```
⬛⬜⬜⬛⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬜⬛⬜⬜⬛⬜⬜⬛
⬜⬛⬜⬜⬜⬜⬛⬜⬜⬜⬜⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬛⬜⬜⬜
-----------------------------------
⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛
⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬛⬜⬜⬛
⬜⬜⬜⬜⬜⬜⬛⬜⬛⬜⬜⬜⬛⬛⬛
⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬛⬜⬜⬛
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬜⬜⬜
```

And after folding the bottom half up, Freddie got the following result:

```
⬛⬜⬜⬛⬜⬜⬛⬜⬛⬜⬜⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬜⬛⬜⬜⬛⬜⬜⬛
⬜⬛⬜⬜⬜⬜⬛⬜⬛⬜⬜⬛⬛⬛⬛
⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬛⬜⬜⬛
⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬛⬜⬜⬛
```

Notice that when folding, some of the black cells overlap, but **a fold line will never contain black cells**. Since
some of the black cells have merged, Freddie was left with 24 black cells instead of 31.

The second instruction, `fold left along x=7`, indicates the following line:

```
⬛⬜⬜⬛⬜⬜⬛| ⬛⬜⬜⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛| ⬛⬜⬜⬛⬜⬜⬛
⬜⬛⬜⬜⬜⬜⬛| ⬛⬜⬜⬛⬛⬛⬛
⬜⬜⬜⬜⬜⬜⬛| ⬜⬜⬜⬛⬜⬜⬛
⬛⬜⬜⬛⬜⬜⬛| ⬜⬜⬜⬛⬜⬜⬛
```

And after folding the right side left, Freddie got the following result and is left with 20 black cells:

```
⬛⬜⬜⬛⬜⬜⬛
⬛⬜⬜⬛⬜⬜⬛
⬛⬛⬛⬛⬜⬜⬛
⬛⬜⬜⬛⬜⬜⬛
⬛⬜⬜⬛⬜⬜⬛
```

Shockingly, after folding, the final result says "HI"! Freddie is definitely on the right track, but the instructions
for the other messages are too big for him to calculate by hand. In order to help Freddie find out where his things
are, write a program that can help him out!

You're more than welcome to use whatever programming language you're most comfortable with. Even though Freddie would
like to get his uniform back as fast as possible, please do not compromise code quality. Include abstractions that you
think are valuable to keep your code clean and reusable (Freddie's friends will probably play tricks on him again!)
Think through edge cases and test scenarios that can help us assert the correctness of your program.

Decode the other secret messages and see if you can help Freddie find out where in the world his uniform is!
