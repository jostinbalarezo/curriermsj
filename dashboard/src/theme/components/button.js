import { mode } from "@chakra-ui/theme-tools"

export const buttonStyles = {
  components: {
    Button: {
      variants: {
        main: {
          bg: "brand.500",
          borderRadius: "16px",
          color: "white",
          _hover: { bg: "brand.400" },
          _active: { bg: "brand.600" },
        },
        brand: {
          bg: "brand.500",
          borderRadius: "16px",
          color: "white",
          _hover: { bg: "brand.400" },
          _active: { bg: "brand.600" },
        },
        darkBrand: {
          bg: "brand.900",
          borderRadius: "16px",
          color: "white",
          _hover: { bg: "brand.800" },
          _active: { bg: "brand.700" },
        },
        lightBrand: {
          bg: "#F2EFFF",
          borderRadius: "16px",
          color: "brand.500",
          _hover: { bg: "#EDE9FF" },
          _active: { bg: "#DDD6FF" },
        },
        light: (props) => ({
          bg: mode("secondaryGray.300", "navy.700")(props),
          borderRadius: "16px",
          color: mode("secondaryGray.900", "white")(props),
          _hover: { bg: mode("secondaryGray.400", "navy.600")(props) },
          _active: { bg: mode("secondaryGray.500", "navy.500")(props) },
        }),
        action: (props) => ({
          fontWeight: "500",
          borderRadius: "50px",
          bg: mode("secondaryGray.300", "brand.400")(props),
          color: mode("brand.500", "white")(props),
          _hover: { bg: mode("secondaryGray.200", "brand.300")(props) },
          _active: { bg: mode("secondaryGray.400", "brand.500")(props) },
        }),
        setup: (props) => ({
          fontWeight: "500",
          borderRadius: "50px",
          bg: mode("transparent", "navy.800")(props),
          border: mode("1px solid", "0px solid"),
          borderColor: mode("secondaryGray.400", "transparent"),
          color: mode("secondaryGray.900", "white")(props),
          _hover: { bg: mode("secondaryGray.300", "navy.700")(props) },
          _active: { bg: mode("secondaryGray.400", "navy.600")(props) },
        }),
      },
    },
  },
}
