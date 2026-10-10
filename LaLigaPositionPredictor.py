from playwright.sync_api import sync_playwright

teams = {
    "FC Barcelona": "https://footystats.org/clubs/fc-barcelona-83",
    "Real Madrid": "https://footystats.org/clubs/real-madrid-cf-84",
    "Atlético Madrid": "https://footystats.org/clubs/club-atletico-de-madrid-117",
    "Villarreal": "https://footystats.org/clubs/villarreal-cf-76",
    "Real Betis": "https://footystats.org/clubs/real-betis-balompie-284",
    "Athletic Club": "https://footystats.org/clubs/athletic-club-bilbao-285",
    "Celta de Vigo": "https://footystats.org/clubs/real-club-celta-de-vigo-281",
    "Valencia CF": "https://footystats.org/clubs/valencia-cf-288",
    "Real Sociedad": "https://footystats.org/clubs/real-sociedad-de-futbol-290",
    "Sevilla FC": "https://footystats.org/clubs/sevilla-fc-98",
    "Deportivo La Coruña": "https://footystats.org/clubs/real-club-deportivo-de-la-coruna-286",
    "RCD Espanyol": "https://footystats.org/clubs/reial-club-deportiu-espanyol-280",
    "Getafe CF": "https://footystats.org/clubs/getafe-club-de-futbol-293",
    "Rayo Vallecano": "https://footystats.org/clubs/rayo-vallecano-291",
    "CA Osasuna": "https://footystats.org/clubs/ca-osasuna-287",
    "RCD Mallorca": "https://footystats.org/clubs/real-club-deportivo-mallorca-298",
    "Deportivo Alavés": "https://footystats.org/clubs/deportivo-alaves-277",
    "Málaga CF": "https://footystats.org/clubs/malaga-cf-283",
    "UD Las Palmas": "https://footystats.org/clubs/ud-las-palmas-276",
    "Real Zaragoza": "https://footystats.org/clubs/real-zaragoza-299",
    "Real Valladolid": "https://footystats.org/clubs/real-valladolid-club-de-futbol-297",
    "Sporting Gijón": "https://footystats.org/clubs/real-sporting-de-gijon-289",
    "Racing Santander": "https://footystats.org/clubs/real-racing-club-de-santander-319",
    "Real Oviedo": "https://footystats.org/clubs/real-oviedo-309",
    "CD Numancia": "https://footystats.org/clubs/cd-numancia-de-soria-306",
    "Real Murcia": "https://footystats.org/clubs/real-murcia-cf-321",
    "UD Salamanca": "https://footystats.org/clubs/ud-salamanca-16149",
    "Hércules CF": "https://footystats.org/clubs/hercules-cf-324",
    "Albacete Balompié": "https://footystats.org/clubs/albacete-balompie-316",
    "Recreativo de Huelva": "https://footystats.org/clubs/real-club-recreativo-de-huelva-318",
    "Gimnàstic de Tarragona": "https://footystats.org/clubs/club-gimnastic-de-tarragona-303",
    "CD Tenerife": "https://footystats.org/clubs/cd-tenerife-311",
    "UD Almería": "https://footystats.org/clubs/ud-almeria-296",
    "Levante UD": "https://footystats.org/clubs/levante-ud-292",
    "Elche CF": "https://footystats.org/clubs/elche-cf-295",
    "Cádiz CF": "https://footystats.org/clubs/cadiz-cf-310",
    "Granada CF": "https://footystats.org/clubs/granada-cf-282",
    "CD Leganés": "https://footystats.org/clubs/cd-leganes-278",
    "Girona FC": "https://footystats.org/clubs/girona-fc-312",
    "SD Eibar": "https://footystats.org/clubs/sd-eibar-279",
    "SD Huesca": "https://footystats.org/clubs/sd-huesca-301",
    "Xerez CD": "https://footystats.org/clubs/xerez-cd-326",
    "Extremadura UD": "https://footystats.org/clubs/extremadura-ud-4589",
    "Mérida AD": "https://footystats.org/clubs/merida-asociacion-deportiva-4601",
    "Mérida UD": "https://footystats.org/clubs/merida-ud-678116",
    "UD Logroñés": "https://footystats.org/clubs/ud-logrones-4500"
}

Laliga = [
    {
        "season": "2017/18",
        "teams": [
            ("Barcelona", 1),
            ("Atlético Madrid", 2),
            ("Real Madrid", 3),
            ("Valencia", 4),
            ("Villarreal", 5),
            ("Real Betis", 6),
            ("Sevilla", 7),
            ("Getafe", 8),
            ("Eibar", 9),
            ("Girona", 10),
            ("Espanyol", 11),
            ("Real Sociedad", 12),
            ("Celta Vigo", 13),
            ("Alavés", 14),
            ("Levante", 15),
            ("Athletic Club", 16),
            ("Leganés", 17),
            ("Deportivo La Coruña", 18),
            ("Las Palmas", 19),
            ("Málaga", 20)
        ]
    },

    {
        "season": "2018/19",
        "teams": [
            ("Barcelona", 1),
            ("Atlético Madrid", 2),
            ("Real Madrid", 3),
            ("Valencia", 4),
            ("Getafe", 5),
            ("Sevilla", 6),
            ("Espanyol", 7),
            ("Athletic Club", 8),
            ("Real Sociedad", 9),
            ("Real Betis", 10),
            ("Alavés", 11),
            ("Eibar", 12),
            ("Leganés", 13),
            ("Villarreal", 14),
            ("Levante", 15),
            ("Valladolid", 16),
            ("Celta Vigo", 17),
            ("Girona", 18),
            ("Huesca", 19),
            ("Rayo Vallecano", 20)
        ]
    },

    {
        "season": "2019/20",
        "teams": [
            ("Real Madrid", 1),
            ("Barcelona", 2),
            ("Atlético Madrid", 3),
            ("Sevilla", 4),
            ("Villarreal", 5),
            ("Real Sociedad", 6),
            ("Granada", 7),
            ("Getafe", 8),
            ("Valencia", 9),
            ("Osasuna", 10),
            ("Athletic Club", 11),
            ("Levante", 12),
            ("Valladolid", 13),
            ("Eibar", 14),
            ("Real Betis", 15),
            ("Alavés", 16),
            ("Celta Vigo", 17),
            ("Leganés", 18),
            ("Mallorca", 19),
            ("Espanyol", 20)
        ]
    },

    {
        "season": "2020/21",
        "teams": [
            ("Atlético Madrid", 1),
            ("Real Madrid", 2),
            ("Barcelona", 3),
            ("Sevilla", 4),
            ("Real Sociedad", 5),
            ("Real Betis", 6),
            ("Villarreal", 7),
            ("Celta Vigo", 8),
            ("Granada", 9),
            ("Athletic Club", 10),
            ("Osasuna", 11),
            ("Cádiz", 12),
            ("Valencia", 13),
            ("Levante", 14),
            ("Getafe", 15),
            ("Alavés", 16),
            ("Elche", 17),
            ("Huesca", 18),
            ("Valladolid", 19),
            ("Eibar", 20)
        ]
    },

    {
        "season": "2021/22",
        "teams": [
            ("Real Madrid", 1),
            ("Barcelona", 2),
            ("Atlético Madrid", 3),
            ("Sevilla", 4),
            ("Real Betis", 5),
            ("Real Sociedad", 6),
            ("Villarreal", 7),
            ("Athletic Club", 8),
            ("Valencia", 9),
            ("Osasuna", 10),
            ("Celta Vigo", 11),
            ("Rayo Vallecano", 12),
            ("Elche", 13),
            ("Espanyol", 14),
            ("Getafe", 15),
            ("Mallorca", 16),
            ("Cádiz", 17),
            ("Granada", 18),
            ("Levante", 19),
            ("Alavés", 20)
        ]
    },

    {
        "season": "2022/23",
        "teams": [
            ("Barcelona", 1),
            ("Real Madrid", 2),
            ("Atlético Madrid", 3),
            ("Real Sociedad", 4),
            ("Villarreal", 5),
            ("Real Betis", 6),
            ("Osasuna", 7),
            ("Athletic Club", 8),
            ("Mallorca", 9),
            ("Girona", 10),
            ("Rayo Vallecano", 11),
            ("Sevilla", 12),
            ("Celta Vigo", 13),
            ("Cádiz", 14),
            ("Getafe", 15),
            ("Valencia", 16),
            ("Almería", 17),
            ("Valladolid", 18),
            ("Espanyol", 19),
            ("Elche", 20)
        ]
    },

    {
        "season": "2023/24",
        "teams": [
            ("Real Madrid", 1),
            ("Barcelona", 2),
            ("Girona", 3),
            ("Atlético Madrid", 4),
            ("Athletic Club", 5),
            ("Real Sociedad", 6),
            ("Real Betis", 7),
            ("Villarreal", 8),
            ("Valencia", 9),
            ("Alavés", 10),
            ("Osasuna", 11),
            ("Getafe", 12),
            ("Celta Vigo", 13),
            ("Sevilla", 14),
            ("Mallorca", 15),
            ("Las Palmas", 16),
            ("Rayo Vallecano", 17),
            ("Cádiz", 18),
            ("Almería", 19),
            ("Granada", 20)
        ]
    },

    {
        "season": "2024/25",
        "teams": [
            ("Barcelona", 1),
            ("Real Madrid", 2),
            ("Atlético Madrid", 3),
            ("Athletic Club", 4),
            ("Villarreal", 5),
            ("Real Betis", 6),
            ("Celta Vigo", 7),
            ("Rayo Vallecano", 8),
            ("Osasuna", 9),
            ("Mallorca", 10),
            ("Real Sociedad", 11),
            ("Valencia", 12),
            ("Getafe", 13),
            ("Espanyol", 14),
            ("Alavés", 15),
            ("Girona", 16),
            ("Sevilla", 17),
            ("Leganés", 18),
            ("Las Palmas", 19),
            ("Valladolid", 20)
        ]
    },

    {
        "season": "2025/26",
        "teams": [
            {'team': "Barcelona", 'position': 1},
            {'team': "Real Madrid", 'position': 2},
            ("Villarreal", 3),
            ("Atlético Madrid", 4),
            ("Real Betis", 5),
            ("Celta Vigo", 6),
            ("Getafe", 7),
            ("Rayo Vallecano", 8),
            ("Valencia", 9),
            ("Real Sociedad", 10),
            ("Espanyol", 11),
            ("Athletic Club", 12),
            ("Sevilla", 13),
            ("Alavés", 14),
            ("Elche", 15),
            ("Levante", 16),
            ("Osasuna", 17),
            ("Mallorca", 18),
            ("Girona", 19),
            ("Real Oviedo", 20)
        ]
    }
]

teamsamples = []


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    pages = laliga_2019_20_links = [
    "https://footystats.org/clubs/real-madrid-cf-84",
    "https://footystats.org/clubs/fc-barcelona-83",
    "https://footystats.org/clubs/club-atletico-de-madrid-117",
    "https://footystats.org/clubs/sevilla-fc-98",
    "https://footystats.org/clubs/villarreal-cf-76",
    "https://footystats.org/clubs/real-sociedad-de-futbol-290",
    "https://footystats.org/clubs/granada-cf-282",
    "https://footystats.org/clubs/getafe-club-de-futbol-293",
    "https://footystats.org/clubs/valencia-cf-288",
    "https://footystats.org/clubs/ca-osasuna-287",
    "https://footystats.org/clubs/athletic-club-bilbao-285",
    "https://footystats.org/clubs/levante-ud-292",
    "https://footystats.org/clubs/real-betis-balompie-284",
    "https://footystats.org/clubs/real-club-celta-de-vigo-281",
    "https://footystats.org/clubs/deportivo-alaves-277",
    "https://footystats.org/clubs/real-valladolid-club-de-futbol-297",
    "https://footystats.org/clubs/sd-eibar-279",
    "https://footystats.org/clubs/real-club-deportivo-mallorca-298",
    "https://footystats.org/clubs/leganes-278",
    "https://footystats.org/clubs/reial-club-deportiu-espanyol-280"
]

    for page_url in pages:
        page.goto(page_url)
        
        n_laliga = 2
        
        features = ['xG For / Match', 
                        'xG Against / Match', 
                        'Scored / Match', 
                        'Conceded / Match', 
                        'Clean Sheets %', 
                        'Failed to Score %', 
                        'Possession AVG',
                        'Shots Taken / Match',
                        'Shots Conversion Rate',
                        'Goal Kicks / Match']
        
        for i in range(1, n_laliga):
                page.locator(
                    '//*[@id="h2h_content1"]/div/div/div[2]/div[3]/div[2]/div[1]'
                ).click()
        
                page.wait_for_timeout(2000)
        
                button = page.locator(
                                    f'//*[@id="h2h_content1"]/div/div/div[2]/div[3]/div[2]/div[2]/button[7]'
                        )

                season = button.text_content()

                print(season)

                button.click()
        
                page.wait_for_timeout(15000)
        
                season_stats = []
        
                for j in range(19):
                    liga = page.locator('//*[@id="h2h_content3"]/div[1]/div/a').text_content().strip()
                    
                    print(liga)
                    
                    if liga != 'La Liga Table':
                        print('Time de merda')
                        continue

                    try:
                        row_name = page.locator(
                        f'//*[@id="overview-0"]/table/tbody/tr[{j+1}]/td[1]').inner_text()
                        print(row_name)
                        if row_name in features:
                            team = page.locator(
                            f'//*[@id="overview-0"]/table/tbody/tr[{j+1}]/td[2]'
                            ).text_content()
                            season_stats.append(team)
                    except:
                        pass
                                        
        
                teamsamples.append({
                   "season": season,
                    "team": page.locator('//*[@id="h2h_content1"]/div/div/div[2]/div[2]/h1').text_content(),
                    "stats": season_stats,
                    "position": page.locator('//*[@id="h2h_content1"]/div/div/div[2]/div[2]/p').text_content() 
                })
        
        
    browser.close()
        
    with open('teamsamples2iteration.csv', 'a') as f:
        f.write(str(teamsamples) + "\n")
        
    print(teamsamples)

