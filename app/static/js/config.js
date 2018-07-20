import Axios from "axios";


Axios.defaults.headers.common["X-CSRFToken"] = window.CSRF_TOKEN;
Axios.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";