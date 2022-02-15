from .skodakspotter import skodakspotter

def setup(bot):
    bot.add_cog(skodakspotter(bot))
