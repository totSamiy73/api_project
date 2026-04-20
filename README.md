<h1 align="center">api_project_test</h1>
<h1 align="center">👨‍💻 кратко по запуску</h1>



прогон всех тестов, отчет в консоли:

pytest -vs

прогон с сохранением результатов тестов для allure:

pytest -vs --alluredir=allure-results

генерируем и открываем HTML-отчёт allure в браузере:

allure serve allure-results/ 

генерируем и сохраняем HTML-отчёт allure в папке allure-reports:

allure generate -c allure-results -o allure-reports

прогон smoke:

pytest -vs -m smoke
