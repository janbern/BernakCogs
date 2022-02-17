from .skodakspotter import SkodakSpotter

def setup(bot):
    bot.add_cog(SkodakSpotter(bot))
