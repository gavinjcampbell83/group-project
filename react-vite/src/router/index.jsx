import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import ProductDetailsPage from '../components/ProductDetailsPage';
import Layout from './Layout';
import OpenModalButton from '../components/OpenModalButton/OpenModalButton.jsx'
import CreateReviewModal from '../components/CreateReviewModal/CreateReviewModal.jsx';

// //! dummy for testing
// const user = { id: 1, name: "Test User" }; 
// //!

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <h1>Welcome!</h1>,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "/products/:productid",
        element: <ProductDetailsPage />,
      },
      {
        path: "*",
        element: <h1>Page Does Not Exist</h1>,
      },
      // {
      //   path: "/test-review",
      //   element: (
      //       <div>
      //           <h1>Test the Review Modal</h1>
      //           <OpenModalButton
      //               modalComponent={<CreateReviewModal productId={1} user={user} />}
      //               buttonText="Open Review Modal"
      //           />
      //       </div>
      //   ),
      // }
    ],
  },
]);