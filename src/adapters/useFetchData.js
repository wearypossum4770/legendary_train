/** @format */

import { useEffect, useState } from "react";
export default function useFetchData({ url, options, needsFetch }) {
  const [response, setResponse] = useState();
  const [errors, setErrors] = useState();
  useEffect(() => {
    let opts = { ...options, mode: "cors", method: "GET" };
    async function fetchData() {
      try {
        const resp = await (await fetch(url, opts)).json();
        setResponse(resp);
      } catch (err) {
        setErrors(err);
      }
    }
    if (needsFetch) {
      fetchData();
    }
  }, [needsFetch, setResponse, setErrors, options, url]);
  return { response: response, errors: errors };
}
