from redbot.core import commands

class skodakspotter(commands.Cog):
    """Je Stegomrd online?"""

    def __init__(self, bot):
		self.bot = bot

    @commands.command()
    async def skodak(self, ctx):

        import requests
        from bs4 import BeautifulSoup
		

        URL = 'http://armory.twinstar.cz/character-feed.xml?r=Apollo&cn=Stegomrd'
        page = requests.get(URL)
        soup = BeautifulSoup(page.text, 'xml')
        timestamp = soup.find('character')
        
		await ctx.send(timestamp['lastModified'])
