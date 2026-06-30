import { mode } from "@chakra-ui/theme-tools"

export const inputStyles = {
  components: {
    Input: {
      variants: {
        auth: (props) => ({
          field: {
            bg: mode("white", "navy.700")(props),
            border: "1px solid",
            borderColor: mode("secondaryGray.100", "rgba(135, 140, 189, 0.3)"),
            borderRadius: "15px",
            fontSize: "sm",
            _placeholder: { color: mode("secondaryGray.600", "secondaryGray.600") },
          },
        }),
        main: (props) => ({
          field: {
            bg: mode("white", "navy.700")(props),
            border: "1px solid",
            borderColor: mode("secondaryGray.100", "rgba(135, 140, 189, 0.3)"),
            borderRadius: "16px",
            fontSize: "sm",
            _placeholder: { color: mode("secondaryGray.600", "secondaryGray.600") },
          },
        }),
        search: (props) => ({
          field: {
            bg: mode("white", "navy.700")(props),
            border: "1px solid",
            borderColor: mode("secondaryGray.100", "rgba(135, 140, 189, 0.3)"),
            borderRadius: "30px",
            fontSize: "sm",
            _placeholder: { color: mode("secondaryGray.600", "secondaryGray.600") },
          },
        }),
      },
    },
  },
}
