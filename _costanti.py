_CITIES = {}

_CITIES['africa'] = ['kinshasa', 'lagos', 'cairo', 'giza', 'johannesburg', 'rabat', 'casablanca', 'dakar',
                    'nairobi', 'capetown', 'tripoli', 'luanda', 'addis_ababa']

_CITIES['asia'] = ['tokyo', 'delhi', 'shanghai', 'dhaka', 'mumbai', 'beijing', 'osaka', 'seoul', 'istanbul',
                  'islamabad', 'bangkok', 'singapore', 'jakarta', 'dubai', 'baghdad', 'kabul', 'pyongyang',
                  'ulaanbaatar', 'kathmandu', 'tehran', 'hanoi']

_CITIES['australia'] = ['melbourne', 'sydney', 'perth', 'wellington']

_CITIES['europe'] = ['london', 'cardiff', 'belfast', 'edinburgh', 'dublin', 'birmingham', 'leeds', 'glasgow',
                    'sheffield', 'berlin', 'hamburg', 'munich', 'frankfurt', 'stuttgart', 'rome', 'milan',
                    'florence', 'naples', 'turin', 'messina', 'bologna', 'madrid', 'barcelona', 'zurich',
                    'paris', 'lyon', 'marseille', 'toulouse', 'moscow', 'saint_petersburg', 'krakow',
                    'warsaw', 'lisbon', 'porto', 'amsterdam', 'stockholm', 'belgrade', 'vienna', 'oslo',
                    'budapest', 'copenhagen', 'athens', 'helsinki', 'tallinn', 'kyiv', 'prague', 'brussels',
                    'tirana', 'bucharest', 'vilnius', 'riga', 'reykjavik', 'bratislava', 'luxembourg']

_CITIES['north_america'] = ['new_york', 'los_angeles', 'chicago', 'houston', 'phoenix', 'philadelphia',
                           'san_antonio', 'san_diego', 'dallas', 'austin', 'jacksonville', 'fort_worth',
                           'indianapolis', 'charlotte', 'san_francisco', 'seattle', 'denver', 'washington',
                           'nashville', 'el_paso', 'boston', 'portland', 'detroit', 'memphis', 'kansas_city',
                           'new_orleans', 'miami', 'honolulu', 'ottawa', 'toronto', 'montreal', 'vancouver',
                           'havana', 'la_vegas']

_CITIES['south_america'] = ['bogota', 'caracas', 'lima', 'brasilia', 'quito', 'montevideo', 'buenos_aires',
                           'la_paz', 'sao_paulo', 'santiago_chile', 'rio_janeiro']

_TOT_CITIES = [item for sublist in list(_CITIES.values()) for item in sublist]


_REVERSE_CITIES = {}
for continent in _CITIES:
    _REVERSE_CITIES.update({city: continent for city in _CITIES[continent]})


# -----------------------------



_TOPIC = {}

_TOPIC['crime'] = ['abduction', 'arson', 'assassination', 'blackmail', 'bombing', 'bribery', 'burglary', 'child_abuse',
                   'corruption', 'cybercrime', 'domestic_violence', 'drunk_driving', 'espionage', 'fraud', 'genocide',
                   'hijacking', 'homicide', 'hooliganism', 'kidnapping', 'looting', 'manslaughter', 'mugging', 'murder',
                   'poaching', 'rape', 'riot', 'robbery', 'pickpocket', 'shoplifting', 'smuggling', 'speeding', 'terrorism',
                   'theft', 'prostitution', 'treason', 'vandalism', 'money_laundering', 'tax_evasion']

_TOPIC['education'] = ['education', 'school', 'high_school', 'university', 'student', 'professor', 'teacher', 'college',
                       'schooling', 'graduate', 'undergraduate', 'undergrad', 'teaching', 'instruction', 'pedagogy',
                       'learning', 'university', 'schooling', 'literature', 'educational', 'knowledge', 'research',
                       'homework', 'degree', 'diploma']

_TOPIC['food'] = ['restaurant', 'cuisine', 'chef', 'gourmet', 'meal', 'cooking', 'recipe', 'culinary', 'diner',
                  'lunch', 'dinner', 'cafe', 'bistro', 'baking', 'foodstuff', 'meat', 'steakhouse', 'pizzeria',
                  'restaurateur', 'brasserie', 'chef', 'seafood', 'baker' , 'butcher']

_TOPIC['work'] = ['job', 'work', 'salary', 'business', 'career', 'office', 'secretary', 'colleague', 'profession', 'industry',
                  'company', 'corporation', 'businessman', 'entrepreneur', 'manager', 'employee', 'worker', 'wage', 'director',
                  'labour', 'task', 'assignment', 'commission', 'project', 'operate']

_TOPIC['nightlife'] = ['nightlife', 'pub', 'bar', 'disco', 'club', 'cinema', 'movie', 'festival', 'nightclub', 'nightspot',
                       'discotheque', 'cabaret', 'saloon', 'theatre', 'theater', 'joint', 'auditorium']

_TOPIC['cold'] = ['cold', 'snow', 'freeze', 'ice', 'hailstorm', 'frost', 'avalanche', 'blizzard', 'winter']

_TOPIC['hot'] = ['hot', 'sun', 'sweat', 'torrid', 'warm', 'dry', 'drought', 'summer']

_TOPIC['transport'] = ['taxi', 'plane', 'airplane', 'bus', 'subway', 'aviation', 'airline', 'train',
                                   'boat', 'pullman', 'funicular', 'gondola']

_TOPIC['environment'] = ['ecology', 'sustainability', 'organic', 'renewable', 'ecological', 'biodegradable', 'recyclable',
                         'atmosphere', 'environment', 'ecosystem', 'agronomy', 'agroforestry', 'biosphere', 'bio', 'biological']

_TOPIC['pollution'] = ['pollution', 'waste', 'toxic', 'toxin', 'impurity', 'contaminant', 'contamination', 'foulness',
                       'smog', 'dioxide', 'sulfur', 'emission', 'eutrophication', 'deforestation']

_TOPIC['history'] = ['king', 'queen', 'historical', 'castle', 'ruin', 'church', 'philosophy', 'medieval', 'history', 'knight',
                     'museum', 'temple', 'antiquity', 'ancient', 'cathedral', 'monument', 'archeological', 'tradition',
                     'culture', 'amphitheater']

_TOPIC['gambling'] = ['gambling', 'game', 'luck', 'chance', 'card', 'roulette', 'casino', 'blackjack', 'poker', 'slot',
                      'gambler', 'wagering', 'croupier', 'bet', 'bookie', 'bookmaker', 'speculator', 'risk_taking',
                      'high_roller', 'solitaire', 'baccarat', 'bingo']

_TOPIC['alcohol'] = ['alcohol', 'alcoholic', 'binge_drinking', 'drunk', 'drunkenness', 'liquor', 'beer', 'cocktail', 'rum',
                     'vodka', 'tequila', 'gin', 'whisky', 'whiskey', 'brandy', 'scotch', 'bourbon', 'champagne', 'booze',
                     'alcoholic_beverage', 'alcohol_consumption', 'firewater', 'nightcap', 'brew', 'wine']
					# 'martini', 'cerveza', 'anejo', 'cointreau', 'sangria', 'mezcal', 'jagermeister', 'limoncello', 'heineken', 'cachaca', 'mojito']

_TOPIC['music'] = ['dance', 'music', 'jazz', 'reggaeton', 'song', 'melody', 'musical', 'reggae', 'hip_hop', 'rap', 'rapper',
                   'singer', 'rock_roll', 'lyrics', 'ballad', 'pop', 'k_pop', 'alternative', 'samba', 'techno', 'podcast',
                   'punk', 'funky', 'gospel', 'electro']

_TOPIC['fitness'] = ['fitness', 'health', 'healthy', 'aerobics', 'workout', 'cardio', 'jogging', 'climbing', 'trekking',
                     'weight_training', 'strength_training', 'hike', 'wellness', 'yoga', 'pilates', 'toning', 'training',
                     'gym', 'aerobic', 'exercise', 'muscular', 'athletic']

_TOPIC['vegetation'] = ['vegetation', 'tree', 'forest', 'rainforest', 'grassland', 'fir', 'pine', 'oak', 'acre', 'greenery',
                       'field', 'garden', 'flower', 'greenery', 'plant', 'park', 'prairie', 'alps', 'hill', 'mountain', 'oasis',
                       'farmer', 'gardener', 'florist']

_TOPIC['animals'] = ['safari', 'zoo', 'animal', 'wild', 'wildlife', 'aquarium', 'fauna', 'reptile', 'mammal', 'bovine',
                     'primate', 'insect', 'pet', 'creature', 'bird', 'invertebrate', 'megafauna', 'seaworld', 'zoological']
                    # 'cat', 'dog', 'elephant', 'lion', 'giraffe', 'koala', 'gorilla', 'panda', 'sawfish', 'whale', 'shark', 'dolphin',

_TOPIC['sport'] = ['soccer', 'football', 'basketball', 'volleyball', 'golf', 'baseball', 'hockey', 'bowling', 'ping_pong',
                   'tennis', 'swimming', 'boxing', 'skiing', 'rugby', 'surfing', 'karate', 'snowboarding', 'judo',
                   'badminton', 'athlete', 'sport', 'wrestling', 'racing', 'marathon', 'skating', 'canoe', 'kayak']

_TOPIC['fashion'] = ['hairdresser', 'hairstylist', 'stylist', 'manicure', 'pedicure', 'makeup', 'lipstick', 'mascara',
                     'eyeliner', 'nail_polish', 'tailor']

_TOPIC['tech'] = ['laptop', 'technology', 'smartphone', 'digital', 'television', 'computer', 'server', 'headphone',
                  'monitor', 'start_up', 'wireless', 'software', 'hardware', 'ebook']

# _TOPIC['professions'] = ['fireman', 'journalist', 'lawyer', 'mason', 'mechanic', 'plumber', 'policeman', 'postman', 'soldier',
#                          'taxi_driver', 'waiter', 'engineer', 'doctor', 'nurse', 'goldsmith', 'actor', 'cleaner', 'author',
#                          'astronomer', 'architect', 'dentist', 'designer', 'electrician', 'judge', 'librarian', 'lifeguard',
#                          'painter', 'pharmacist', 'politician', 'photographer', 'scientist', 'receptionist']


_TOT_TOPIC = [item for sublist in list(_TOPIC.values()) for item in sublist]


_REVERSE_TOPIC = {}
for topic in _TOPIC:
    _REVERSE_TOPIC.update({word: topic for word in _TOPIC[topic]})



# -----------------------------



_TOPIC_COLOR = {}
_TOPIC_COLOR['fitness'] = (240, 163, 255)
_TOPIC_COLOR['nightlife'] = (0, 117, 220)
_TOPIC_COLOR['alcohol'] = (153, 63, 0)
_TOPIC_COLOR['gambling'] = (76, 0, 92)
_TOPIC_COLOR['pollution'] = (25, 25, 25)
_TOPIC_COLOR['vegetation'] = (0, 92, 49)
_TOPIC_COLOR['environment'] = (43, 206, 72)
_TOPIC_COLOR['animals'] = (255, 204, 153)
_TOPIC_COLOR['work'] = (128, 128, 128)
_TOPIC_COLOR['professions'] = (143, 124, 0)
_TOPIC_COLOR['education'] = (157, 204, 0)
_TOPIC_COLOR['sport'] = (194, 0, 136)
_TOPIC_COLOR['food'] = (255, 164, 5)
_TOPIC_COLOR['music'] = (255, 168, 187)
_TOPIC_COLOR['crime'] = (255, 0, 16)
_TOPIC_COLOR['cold'] = (94, 241, 242)
_TOPIC_COLOR['sport'] = (0, 153, 143)
_TOPIC_COLOR['public_transportation'] = (153, 0, 0)
_TOPIC_COLOR['history'] = (247, 226, 32)
_TOPIC_COLOR['hot'] = (255, 80, 5)
_TOPIC_COLOR['fashion'] = (190, 88, 245)
_TOPIC_COLOR['tech'] = (103, 70, 115)


_CITY_COLOR = {}
_CITY_COLOR['asia'] = (245, 239, 66)
_CITY_COLOR['africa'] = (115, 75, 23)
_CITY_COLOR['australia'] = (5, 100, 242)
_CITY_COLOR['europe'] = (17, 133, 50)
_CITY_COLOR['north_america'] = (247, 32, 54)
_CITY_COLOR['south_america'] = (32, 179, 179)
