import React from "react"
import { Flex } from "@chakra-ui/react"
import { SidebarResponsive } from "components/sidebar/Sidebar"

export default function NavbarLinksAdmin(props) {
  const { routes } = props

  return (
    <Flex
      w={{ sm: "100%", md: "auto" }}
      alignItems="center"
      flexDirection="row"
    >
      <SidebarResponsive routes={routes} />
    </Flex>
  )
}
