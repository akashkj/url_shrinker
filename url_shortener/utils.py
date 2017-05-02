from .models import Url


BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_usable_shortcode():
	id_to_encode = get_last_inserted_id() + 1
	usable_shortcode = encode(id_to_encode)
	return usable_shortcode


def get_url_for_shortcode(shortcode):
	id_of_url = decode(shortcode)
	try:
		return Url.objects.get(id=id_of_url).url
	except Exception:
		return None


def get_last_inserted_id():
	try:
		return Url.objects.latest('id').id
	except Url.DoesNotExist:
		return 0


def encode(num, char_set=BASE62):
	if num == 0:
		return char_set[0]
	arr = []
	base = len(char_set)
	while num:
		num, rem = divmod(num, base)
		arr.append(char_set[rem])
	arr.reverse()
	return ''.join(arr)


def decode(hash_string, char_set=BASE62):
	base = len(char_set)
	hash_size = len(hash_string)
	num = 0
	idx = 0
	for char in hash_string:
		power = (hash_size - (idx + 1))
		num += char_set.index(char) * (base ** power)
		idx += 1
	return num
