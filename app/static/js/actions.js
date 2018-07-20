import Axios from "axios";
import Promise from "promise";
import Qs from "qs";


module.exports = {
  login: (email, password) => {
    return new Promise((resolve, reject) => {
      Axios.post(API.session, Qs.stringify({ email, password }))
        .then((resp) => {
          resolve();
        })
        .catch((error) => {
          const data = error.response.data;

          if(data.status == null)
            throw 0;

          reject({
            formError: data.msg,
            fieldErrors: data.fields || {}
          });
        })
        .catch((error) => {
          reject({
            formError: "An unexpected error occurred.",
            fieldErrors: {}
          });
        });
    });
  }
}