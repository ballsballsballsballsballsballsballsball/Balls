import random
import discord
import praw as redditballs
from discord.ext import commands as BallsCommands

class RedditMemes(BallsCommands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @BallsCommands.command()
    async def meme(self, ctx):
        reddit = redditballs.Reddit(
            client_id='balls',
            client_secret='balls',
            user_agent='balls',
            check_for_async=False
        )
        memes = reddit.subreddit('dankmemes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(post_to_pick):
            submission = next(x for x in memes if not x.stickied)
        ballsEmbed = discord.Embed(
            color=0x842899
        )
        ballsEmbed.add_field(name=f'New post in r/balls',
                            value=f'[{submission.title}](https://reddit.com{submission.permalink})', inline=False)
        ballsEmbed.add_field(name='Author:', value=f'u/{submission.author}(jk its u/balls)', inline=False)
        ballsEmbed.set_image(url=submission.url)
        ballsEmbed.set_footer(text=f'''{submission.score}👍 | {submission.num_comments}💬''')
        await ctx.send(embed=ballsEmbed)


def setup(bot):
    bot.add_cog(RedditMemes(bot))
