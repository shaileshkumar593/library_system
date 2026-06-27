import "./globals.css";

import Navbar from "../components/Navbar";

import QueryProvider from "../providers/QueryProvider";

export default function RootLayout({

children,

}:{

children:React.ReactNode

}){

return(

<html>

<body>

<QueryProvider>

<Navbar/>

{children}

</QueryProvider>

</body>

</html>

)

}