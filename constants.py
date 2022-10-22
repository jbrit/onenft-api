import re

COLLECTION_CATEGORIES = ['art', 'music', 'trading card', 'collectibles', 'photography', 'virtual world', None]
ADDRESS_REGEX = re.compile('^0x[a-fA-F0-9]{40}$')