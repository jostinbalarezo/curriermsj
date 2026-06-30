import React from "react"
import {
  Box,
  Flex,
  Drawer,
  DrawerBody,
  Icon,
  DrawerOverlay,
  useDisclosure,
  DrawerContent,
  DrawerCloseButton,
} from "@chakra-ui/react"
import Content from "./components/Content"
import { IoMenuOutline } from "react-icons/io5"

function Sidebar(props) {
  const { routes } = props
  let shadow = "unset"
  let sidebarBg = "navy.800"

  return (
    <Box display={{ sm: "none", xl: "block" }} w="100%" position="fixed" minH="100%">
      <Box
        bg={sidebarBg}
        w="300px"
        h="100vh"
        m="0px"
        minH="100%"
        overflowX="hidden"
        boxShadow={shadow}
      >
        <Content routes={routes} />
      </Box>
    </Box>
  )
}

export function SidebarResponsive(props) {
  let sidebarBackgroundColor = "navy.800"
  let menuColor = "white"
  const { isOpen, onOpen, onClose } = useDisclosure()
  const btnRef = React.useRef()
  const { routes } = props

  return (
    <Flex display={{ sm: "flex", xl: "none" }} alignItems="center">
      <Flex ref={btnRef} w="max-content" h="max-content" onClick={onOpen}>
        <Icon
          as={IoMenuOutline}
          color={menuColor}
          my="auto"
          w="20px"
          h="20px"
          me="10px"
          _hover={{ cursor: "pointer" }}
        />
      </Flex>
      <Drawer
        isOpen={isOpen}
        onClose={onClose}
        placement={document.documentElement.dir === "rtl" ? "right" : "left"}
        finalFocusRef={btnRef}
      >
        <DrawerOverlay />
        <DrawerContent w="285px" maxW="285px" bg={sidebarBackgroundColor}>
          <DrawerCloseButton
            zIndex="3"
            onClose={onClose}
            _focus={{ boxShadow: "none" }}
            _hover={{ boxShadow: "none" }}
          />
          <DrawerBody maxW="285px" px="0rem" pb="0">
            <Content routes={routes} />
          </DrawerBody>
        </DrawerContent>
      </Drawer>
    </Flex>
  )
}

export default Sidebar
