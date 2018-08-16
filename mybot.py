import praw


r = praw.Reddit(user_agent='SubReddit_Linker_Bot v0.1',
                  client_id='y5EEYew-UJI-ow',
                  client_secret='SWITCH',
                  username='SWITCH',
                  password='SWITCH')





def alreadyPosted(subm):
	with open("PostedOn.txt","r+") as searchfile:
		for line in searchfile:
			if subm.id == line.strip('\n'):
				return True
	return False

subReddits = ["all","popular","funny","todayilearned","worldnews","gaming","videos","movies","aww","Music","gifs",
"news","EarthPorn","television","pics", "WTF","interestingasfuck","iamverysmart","HumansBeingBros","DIY","nottheonion","UpliftingNews",
"space","Jokes","sports","dataisbeautiful","GetMotivated","bestof","politics","CrappyDesign","bestof","showerThoughts","natureisfuckinglit","hmmm"]

for subsTitle in subReddits:
	subreddit=r.subreddit(subsTitle)
	print ("SubsTitle: "+subsTitle)
	#search through top 100 posts
	for submission in subreddit.rising(limit=20):
		#see if there is a subreddit mentioned in the post title
		#get the subreddit's name
		if 'r/' in submission.title:
			print ("    rising: subreddit reference found in title")
			if(alreadyPosted(submission)==False):
				newWord = ''
				text = submission.title.split('r/',1)[1]
				for letter in text:
					if letter.isalpha():
						newWord +=letter
					else:
						break;
				#Checks if the refrence in the title is to the current subreddit
				if (newWord !=subsTitle):
					post = submission.comments
					#checks if the post has at least 4 comments on it
					if ((len(post))>4):	
						postedOnFile=open("PostedOn.txt","a+")
						postedOnFile.write(submission.id+"\n")
						print ('		Posting: /r/'+newWord)
						submission.reply("For the lazy and those on mobile: "+'/r/'+newWord+'\n\n'+'Beep Boop Bop I am a bot. I post links to subreddits from the post\'s title')
					else:
						print ("	less than 4 comments")
				else:
					print("		self-refrence to subReddit")
			else:
				print("		already posted here")

for submission in subreddit.hot(limit=20):
		#see if there is a subreddit mentioned in the post title
		#get the subreddit's name
		if 'r/' in submission.title:
			print ("    subreddit reference found in title")
			if(alreadyPosted(submission)==False):
				newWord = ''
				text = submission.title.split('r/',1)[1]
				for letter in text:
					if letter.isalpha():
						newWord +=letter
					else:
						break;
				#Checks if the refrence in the title is to the current subreddit
				if (newWord !=subsTitle):
					post = submission.comments
					#checks if the post has at least 4 comments on it
					if ((len(post))>4):	
						postedOnFile=open("PostedOn.txt","a+")
						postedOnFile.write(submission.id+"\n")
						print ('		Posting: /r/'+newWord)
						submission.reply("For the lazy and those on mobile: "+'/r/'+newWord+'\n\n'+'Beep Boop Bop I am a bot. I post links to subreddits from the post\'s title')
					else:
						print ("	less than 4 comments")

