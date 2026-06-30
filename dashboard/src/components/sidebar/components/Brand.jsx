import { Flex } from "@chakra-ui/react"
import { CurrierLogo } from "components/icons/Icons"
import { HSeparator } from "components/separator/Separator"

export function SidebarBrand() {
  return (
    <Flex align="center" direction="column">
      <CurrierLogo h="26px" w="175px" my="32px" color="white" />
      <HSeparator mb="20px" />
    </Flex>
  )
}

export default SidebarBrand
