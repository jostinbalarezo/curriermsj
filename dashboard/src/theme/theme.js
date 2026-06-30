import { extendTheme } from "@chakra-ui/react"
import { CardComponent } from "./additions/card/card"
import { buttonStyles } from "./components/button"
import { badgeStyles } from "./components/badge"
import { inputStyles } from "./components/input"
import { breakpoints } from "./foundations/breakpoints"
import { globalStyles } from "./styles"

export default extendTheme(
  {
    config: {
      initialColorMode: "dark",
      useSystemColorMode: false,
    },
  },
  { breakpoints },
  globalStyles,
  badgeStyles,
  buttonStyles,
  inputStyles,
  CardComponent,
)
