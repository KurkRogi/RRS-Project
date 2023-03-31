const date_field = document.getElementById('id_date');
    date_field.addEventListener('blur', check_available_tables);
    const time_field = document.getElementById('id_time');
    time_field.addEventListener('blur', check_available_tables);
    document.addEventListener('load', check_available_tables);

    function check_available_tables(event) {
        event.preventDefault();
        const field = document.getElementById('id_table');
        const button = document.getElementById('submitButton')  ;  
        const date = date_field.value;
        const time = time_field.value;
        fetch('{% url "bookings:tables_API" %}'+'?date='+date+'&?time='+time, {
            headers: {
                'Accept':'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            }
        }).then(response => {
            return response.json()
        }).then(data => {
            console.log(data)
            if (data.length > 0) {
                {% comment %} field.removeAttribute("disabled");
                button.removeAttribute("disabled");
                for (i in data) {
                    field.innerHTML = `<option value="${i.id}">Table ${i.name} (${i.sits}) ${i.description}</option>`
                }
            } else {
                field.setAttribute("disabled", "");
                button.setAttribute("disabled", "");
                field.innerHTML = `<option value="0">No tables available!</option>` {% endcomment %}
            }
        }).catch(error => {
            console.error('Error: ', error)
        })
    }