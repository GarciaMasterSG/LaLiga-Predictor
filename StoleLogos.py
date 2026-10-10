from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://brandlogos.net/series/2025-26-la-liga-club-logos')

    page.wait_for_selector('.team-logo')

    teams = page.query_selector_all('.team-logo')

    for team in teams:
        page.click(team)
        page.wait_for_timeout(1000)
        page.Locator('//*[@id="dl_svg_action"]').click()
        with page.expect_download() as di:
            page.wait_for_timeout(5000)

        download = di.value

        download.save_as('C:\\Users\\Tusab\\OneDrive\\Documentos\\AMD (Fontys)\\FirstChallengeCode\\LaLigaPredictor\\src\\Crests\\' + download.suggested_filename)

        page.go_back()
        page.go_back()


