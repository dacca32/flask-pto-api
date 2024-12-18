import { createFileRoute } from '@tanstack/react-router'
import { useQuery, queryOptions, useSuspenseQuery } from '@tanstack/react-query'
import { Fragment } from 'react/jsx-runtime'

const profileQueryOptions = queryOptions({
  queryKey: ['profile'],
  queryFn: () => {
    return {
      id: '1',
      name: 'John Doe',
    }
  },
})

export const Route = createFileRoute('/profile/')({
  loader: ({ context: { queryClient } }) =>
    queryClient.ensureQueryData(profileQueryOptions),
  component: Data,
})

function Data() {
  const { data } = useSuspenseQuery(profileQueryOptions)

  return (
    <Fragment>
      <h1>Profile</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </Fragment>
  )
}
