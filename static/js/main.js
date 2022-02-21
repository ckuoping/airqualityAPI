// test
// alert('happy')
const data_panel = document.getElementById("data-panel")
data_panel.addEventListener('click', function(event) {
    console.log(event.target)
    console.log(event.target.parentElement.children[1].innerHTML)
    const show_data_title = document.getElementById('show-data-title')
    const show_data_data = document.getElementById('show-data-data')
    const show_data_date = document.getElementById('show-data-date')
    const show_data_city = document.getElementById('show-data-city')
    const weather_icon = document.getElementById('weather-icon')
    show_data_title.innerHTML = event.target.parentElement.children[0].innerHTML
    show_data_data.innerHTML = 'PM25濃度：' + event.target.parentElement.children[2].innerHTML
    show_data_date.innerHTML = '量測日期：' + event.target.parentElement.children[1].innerHTML
    show_data_city.innerHTML = '所屬城市：' + event.target.parentElement.children[4].innerHTML

    if (parseInt(event.target.parentElement.children[2].innerHTML) > 20) {
        weather_icon.innerHTML = `<i class="fas fa-cloud-meatball"></i>`
    } else {
        weather_icon.innerHTML = `<i class="fas fa-sun"></i>`
    }
})