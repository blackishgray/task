$(() => {
  const fetchapi = () => {
    let customerData = "http://127.0.0.1:8000/api/apis/CustomerData/";
    let branchData = "http://127.0.0.1:8000/api/apis/BranchData/";
    let customerHomeAddressData = "http://127.0.0.1:8000/api/apis/CustomerHomeAddressData/";
    let customerOfficeData = "http://127.0.0.1:8000/api/apis/CustomerOfficeData/";
    let loanAmountData = "http://127.0.0.1:8000/api/apis/LoanAmountData/";

    const apiData = async () => {
      const resp = await fetch(customerData)
      const data = await resp.json()
      console.log(data)
      return data
    }
    apiData()

  }

  fetchapi()
})
