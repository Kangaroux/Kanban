import Axios from "axios";
import Promise from "promise";


function registerUser(data, onError, onSuccess) {
  return new Promise((resolve, reject) => {
    Axios.post(URL.users, data)
      .then((resp) => {
        resolve(resp.data.fields);
      })
      .catch((err) => {
        reject(err.data.msg, err.data.fields);
      });
  });
}