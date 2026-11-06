import { QuartzComponent, QuartzComponentConstructor } from "./types"

const Umami: QuartzComponent = () => {
  return (
    <script
      defer
      src="https://cloud.umami.is/script.js"
      data-website-id="fb835a92-1337-46e6-a13c-eb363975d5f4"
    />
  )
}

export default (() => Umami) satisfies QuartzComponentConstructor