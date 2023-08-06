import discord
import aiohttp
import aiofiles
import requests
import random
import io
import json
from importlib import metadata
import advlink


class Client:
	"""
	The client class for the randseal package containing everything (new in version 2.0.0)
	"""

	def __init__(self, session: aiohttp.ClientSession = None, session2: aiohttp.ClientSession = None, number: int | str | None = None):
		self.session = aiohttp.ClientSession(auto_decompress=False) or session
		self.session2 = aiohttp.ClientSession() or session2

		sealrand = f"{random.randrange(0, 82)}"
		if len(sealrand) == 1:
			sussy = sealrand
			sealrand = "0" + f"{sussy}"
		self.number = number or sealrand
		"""A number between 1 and 82 (New in 1.3.0)"""

	async def asyncFile(self):
		"""
		Returns a `discord.File()` of a seal for py-cord in a non-blocking way (new in version 2.0.0)
		"""
		async with self.session.get(f"https://raw.githubusercontent.com/mariohero24/randseal/fbba6657532d0b6db21c91986843a08a7ab19f26/randseal/00{self.number}.jpg") as r:
			hi = io.BytesIO(await r.read())
			return discord.File(fp=hi, filename=self.number + ".jpg")

	def File(self):
		"""
		Returns a `discord.File()` of a seal for py-cord in a potentially blocking way
		"""
		sealrand = self.number
		r = requests.get(
			f"https://raw.githubusercontent.com/mariohero24/randseal/fbba6657532d0b6db21c91986843a08a7ab19f26/randseal/00{sealrand}.jpg", stream=True)
		return discord.File(fp=io.BytesIO(r.content), filename=sealrand + ".jpg")

	class classEmbed(discord.Embed):
		"""`discord.Embed` subclass (New in 1.3.0)"""

		def __init__(self, title: str | None = None):
			e = Client()
			if title != None:
				super().__init__(colour=e.blank, title=title, url=str(e))
			else:
				super().__init__(colour=e.blank, url=str(e))

	def Embed(self, title: str | None = None):
		"""
		Returns a `discord.Embed()` of a seal which can be edited or used in a message
		"""
		sealrand = self.number
		if title != None:
			return discord.Embed(colour=self.blank, title=title).set_image(url=f"https://raw.githubusercontent.com/mariohero24/randseal/fbba6657532d0b6db21c91986843a08a7ab19f26/randseal/00{sealrand}.jpg")
		else:
			return discord.Embed(colour=self.blank).set_image(url=f"https://raw.githubusercontent.com/mariohero24/randseal/fbba6657532d0b6db21c91986843a08a7ab19f26/randseal/00{sealrand}.jpg")

	async def fetchrole(self, context, id) -> discord.Role:
		"""
		Returns a `discord.Role` that is really just a `discord.Object` for easy use, decided not to edit the class itself because it would be a nightmare to fix (reworked in v2.2.0)
		"""
		return discord.Object(id)

	@property
	def blank(self) -> int:
		return 0x2f3136

	async def jsonload(self, fp:
					aiofiles.threadpool.text.AsyncTextIOWrapper,
					**kwds,
					):
		"""Asynchronous `json.load()` using the `aiofiles` package (New in 1.3.0)"""
		return json.loads(s=await fp.read(), **kwds)

	async def jsondump(
			self,
			obj,
			fp: aiofiles.threadpool.text.AsyncTextIOWrapper,
			**kwds
	):
		"""Asynchronous `json.dump()` using the `aiofiles` package (New in 1.3.0)"""
		e = json.dumps(obj, **kwds)
		await fp.write(e)
		return e

	def __hash__(self):
		return hash(self)

	@property
	def advlink(self):
		return advlink.Link(str(self), session=self.session, session2=self.session2)

	@property
	def url(self):
		return self.advlink.url

	def __str__(self):
		sealrand = self.number
		return f"https://raw.githubusercontent.com/mariohero24/randseal/fbba6657532d0b6db21c91986843a08a7ab19f26/randseal/00{sealrand}.jpg"

	def __eq__(self, obj: object) -> bool:
		return str(self) == str(obj)

	def __int__(self):
		return int(self.number)


__author__: str = "Guard Boi"
"""The author of the package"""

__description__: str = "Generates a random seal image for py-cord"
"""A short description of the package"""

__licence__: str = "MIT"
"""The licence type of the package"""

__version__ = metadata.version("randseal")
"""The version of the package"""

# python3 -m twine upload --repository pypi dist/*
