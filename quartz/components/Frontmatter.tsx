import { QuartzComponentProps, QuartzComponentConstructor } from "./types"

interface Options {
  favouriteNumber: number
}

const defaultOptions: Options = {
  favouriteNumber: 42,
}

export default ((userOpts?: Options) => {
  const opts = { ...userOpts, ...defaultOptions }
  function YourComponent(props: QuartzComponentProps) {
    if (opts.favouriteNumber < 0) {
      return null
    }

    let fm = Object.keys(props.fileData.frontmatter).filter((f) => f[0].toUpperCase() == f[0])

    if (props.fileData.frontmatter?.["Requires"]) {
    }

    return (
      <table>
        {fm.map((f) => (
          <tr>
            <th>{f}</th>
            <td>{props.fileData.frontmatter[f]}</td>
          </tr>
        ))}
      </table>
    )
  }

  return YourComponent
}) satisfies QuartzComponentConstructor
