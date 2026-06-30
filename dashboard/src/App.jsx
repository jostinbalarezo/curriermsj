import React, { useState } from "react"
import { Routes, Route, Navigate } from "react-router-dom"
import { ChakraProvider } from "@chakra-ui/react"
import AdminLayout from "layouts/admin"
import initialTheme from "theme/theme"

export default function Main() {
  const [currentTheme, setCurrentTheme] = useState(initialTheme)
  return (
    <ChakraProvider theme={currentTheme}>
      <Routes>
        <Route
          path="admin/*"
          element={
            <AdminLayout theme={currentTheme} setTheme={setCurrentTheme} />
          }
        />
        <Route path="/" element={<Navigate to="/admin" replace />} />
      </Routes>
    </ChakraProvider>
  )
}
