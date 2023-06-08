Current Road Map:
User input -> Logging System -> Vars -> (Frontend for later) -> DataShaping

May 26th
---------
Not Exactly sure where I am going to go with GymBro but as of right now. GymBro is a program with the intention of tracking workouts, weights, lifts, and other data from the gym. Still working out how far I will take GymBro but ideally I want GymBro to be an app that can show me trends in my workouts and health based on gym data. Currently Working with Supabase.

Right now I'm thinking about how I want to structure this. Ultimately I want want it to be almost exactly like fitnotes but
having a section that shows you info on how you are progressing. So I'm thinking about having a data section where I do all the cool stuff. The logs section will be were new data is stored for lifts. As for the exercises themselves those have to be in there own category. 

Making some progress Right now I just got to figure out how to get column names and apply them when creating a new csv. I've
Figured out how to create new csvs from the names of exercises from the names column but now I have to just create them using
different column names. It's a pretty dumb way tbh but I will figure the better way to do it. 

May 27th
---------
That was a drunk commit lmao

May 28th - May 30th
---------
I was busy and am going to be busy for the next couple of weeks hopefully I'll be able to get some progress not sure what my next step are gonna be. I also I accomplished what I set out to do that day. Now I just gotta figure what to do going forward.

May 31st
---------
Got User input, now I just got to create a better loging system. Also remove spaces in names of files. Goal for Tommorrow is to have a proper logging system setup and then adjusting those vars such that I can use them for their intended purpose. Right now they all are added as strings but some are numbers. Also thing to look into, data will always be date. Once that Is COMPLETELY setup we can, it should be ready for frontend work (which I still have to learn). After logging, we can get started on DataShaping and trends which comes the acc Data Science part.

This is the current roadmap I got planned for the next week or more.



#windows wsl2 - Windows 11 - ubuntu linux

June 1st
----------
I also got to work out how to organize all this like what to make functions and what to make different class files. For now I'm just storing them in files with the name pertaining to what it does.

I just had the biggest monke brain moment ever. Basically wasted a lot of time. I accidentally changed the csvs in a way I didn't want to and I couldn't revert them back. Basically I changed their names so that there were no spaces but it looked unreadable. So Rather than doing something I should've done, I decided to start from scratch again because I did it before and It should be easy. When I went to my old code that I saved, I wasn't there. Only some of it, so I redid everything again and this time the data is actually better. When I went to go save that code in a file I saw that I had a file called 'CreateCsv', which was my old code.... I don't want to talk about it

Might have to look into make the name of exercises into objects. Ex: BenchPress.addSet(parameters:int) will add a new row to the csv

Headers = ['Set': int,'Reps':int,'Weight'int,'Date':str,'Max Lift':int,'Body Weight';int,'Fat%':int,'Phase':str,'Completed':Bool,'Notes':Str]

Set,Reps,Weight,Completed,Notes: Are going to be in every new line inputted by the user
Body Weight,Fat%,Date,Phase: Are going to be at the Top of the day's workout session going to be set unless changed
Max Lift: Some other place going to be automatic

Might have to make another csv for the workout entered that day not sure. Nested csvs :(
If I were to have another csv it would be Headers = ['Workout':file, Date: int, Notes:Str]

I might have to take a small break and think about how I want to proceed with this. Maybe a day or 3.

June 8th
---------
So Apple apparently has taken my idea and made it there own. They are basically using Ai to do what I am trying to do. Bummer. I'm still going to complete this project or at least try to. I think I am going to worry about the UI/UX later and just getting the fundamentals working so now I'm going to work on the Math File to generate images and trends and some other stuff. Once I get that working I can worry about the other stuff. 