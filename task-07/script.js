const apiKey = "ed2d73fa079d57604ef2f7fe56ea2dd5";
const apiUrl = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=";

const searchBox = document.querySelector(".search input");
const searchBtn = document.querySelector(".search button");
const weatherIcon = document.querySelector(".weather-icon");
const weatherConditionText = document.querySelector(".weather-condition"); 

async function checkWeather(city) {
    const response = await fetch(apiUrl + city + `&appid=${apiKey}`);

    if (response.status == 404) {
        document.querySelector(".error").style.display = "block";
        document.querySelector(".weather").style.display = "none";
    } else {
        var data = await response.json();

        document.querySelector(".city").innerHTML = data.name;
        document.querySelector(".temp").innerHTML = Math.round(data.main.temp) + "°C";
        document.querySelector(".humidity").innerHTML = data.main.humidity + "%";
        document.querySelector(".wind").innerHTML = data.wind.speed + " km/h";

        const weatherCondition = data.weather[0].main;
        setWeatherIcon(weatherCondition);

       
        weatherConditionText.innerHTML = `Weather Condition: ${data.weather[0].description}`;

        document.querySelector(".weather").style.display = "block";
        document.querySelector(".error").style.display = "none";
    }
}

function setWeatherIcon(condition) {
    switch (condition) {
        case "Clouds":
            weatherIcon.src = "clouds.png";
            break;
        case "Clear":
            weatherIcon.src = "clear.png";
            break;
        case "Rain":
            weatherIcon.src = "rain.png";
            break;
        case "Drizzle":
            weatherIcon.src = "drizzle.png";
            break;
        case "Mist":
            weatherIcon.src = "mist.png";
            break;
        case "Snow":
            weatherIcon.src = "snow.png";    
            break;
        default:
            weatherIcon.src = ""; 
    }
}

searchBtn.addEventListener("click", () => {
    checkWeather(searchBox.value);
});
