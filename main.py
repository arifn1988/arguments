# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'


# Add your code after this line

def greet(name='Bob' , greeting='Hello, <name>!'):
	new_greeting=greeting.replace('<name>',name)
	return new_greeting


def force(mass,body='earth'):
	planets={
		'sun':274,
		'jupiter':24.9,
		'neptune':11.1,
		'saturn':10.4,
		'earth':9.8,
		'uranus':8.9,
		'venus':8.9,
		'mars':3.7,
		'mercury':3.7,
		'moon':1.6,
		'pluto':0.6
		}
	return planets[body]*mass

def pull(m1,m2,d):
	G = 6.6740 * 10**-11
	return (G*m1*m2)/(d**2)

print(pull(5924*10**24,0.1,6371*10**6))
